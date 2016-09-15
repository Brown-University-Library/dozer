import os
import uuid
import datetime
import urlparse

def _validate_uri(value):
	try:
		urlparse.urlparse(value)
	except:
		raise ValueError("Bad URI: ", value)
	return value

def _validate_int(value):
	if isinstance(value, int):
		return value
	else:
		raise ValueError("Bad int: ",value)

def _validate_datetime(value):
	try:
		datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
	except:	
		raise ValueError("Bad date: ", value)
	return value

def _validate_string(value):
	try:
		value.decode('UTF-8')
	except:
		raise UnicodeError("Bad unicode: ", value)
	return value

class Predicate(object):

	def __init__(self, uri, datatype):
		self.uri = uri
		self.datatype = datatype
		if datatype == 'uri' or datatype == 'anyURI':
			self.validator = _validate_uri
		elif datatype == 'dateTime' or datatype == 'datetime':
			self.validator = _validate_datetime
		elif datatype == 'date':
			self.validator = _validate_datetime
		elif datatype == 'string':
			self.validator = _validate_string
		elif datatype == 'int':
			self.validator = _validate_int

	def validate(self, value):
		return self.validator(value)


def _validate_list(values):
	if not isinstance(values, list):
		raise TypeError('Data must be in list format')
	return values

def _validate_required(values):
	if len(values) == 0:
		raise ValueError("Value is required")
	return values

def _validate_unique(values):
	if len(values) > 1:
		raise ValueError("Only one value permitted")
	return values

class Attribute(object):
	# Add support for "write","edit"; etc
	def __init__(self, predicate, alias=None,
					required=False, optional=False,
					unique=False, allowed=None,
					always=None, only=None):
		self.predicate = predicate
		self.uri = predicate.uri
		self.alias = alias
		self.validators = [_validate_list]
		if presets:
			self.presets = presets
		if required:
			self.required = True
			self.validators.append(_validate_required)
		if unique:
			self.unique = True
			self.validators.append(_validate_unique)
		if always:
			self.always = always
		if allowed:
			self.allowed = allowed

	def set_alias(self, alias):
		self.alias = alias


def rename_dictionary_keys(newKeyMap, dct):
	return { newKeyMap[k]: v for k,v in dct.items() }

def filter_unrecognized_keys(keyList, dct):
	return { k: v for k,v in dct.items() if k in keyList }

def add_missing_keys(keyList, dct):
	out = dct.copy()
	out.update({ k: list() for k in keyList if k not in dct })
	return out

def set_default_list_value(lst, val):
	if not lst:
		return [val]
	else:
		return lst 

def noneify_empty_dictionary_lists(dct):
	noned = { k:set_default_list_value(v, None)
				for k,v in dct.items() }
	return noned

def attribute_builder(aliasDict):
	for alias in aliasDict:
		aliasDict[alias].set_alias(alias)
	return [ attr for attr in aliasDict.values() ]

class Schema(object):
	def __init__(self, attrs):
		if isinstance(attrs, dict):
			attrs = attribute_builder(attrs)
		self.attributes = attrs
		self.aliases = { attr.alias: attr.uri for attr in attrs }
		self.uris = { attr.uri: attr.alias for attr in attrs }
		self.attr_validators = { attr.uri: attr.validators for attr in attrs }
		self.data_validators = { attr.uri: attr.predicate.validator for attr in attrs }
		self.presets = { attr.uri: attr.presets for attr in attrs if hasattr(attr,'presets') }
		self.required = [ attr.uri for attr in attrs if hasattr(attr,'required') ]
		self.optional = [ attr.uri for attr in attrs if not hasattr(attr,'required') ]
		self.datatypes = { attr.uri: attr.predicate.datatype for attr in attrs }

	def unalias_data(self, data):
		return rename_dictionary_keys(self.aliases, data)

	def alias_data(self, data):
		return rename_dictionary_keys(self.uris, data)

	def assign_preset_values(self, data):
		data.update(self.presets)
		return data

	def validate_attributes(self, data):
		out = dict()
		for k, v in data.items():
			validators = self.attr_validators[k]
			filtered = v
			for validator in validators:
				try:
					filtered = validator(filtered)
				except ValueError as e:
					raise Exception(e,k,v)
			out[k] = filtered
		return out

	def validate_data(self, data):
		out = dict()
		for k, v in data.items():
			validator = self.data_validators[k]
			try:
				out[k] = [validator(d) for d in v]
			except ValueError as e:
				raise Exception(e,k,d)
		return out

	def validate_structure(self, data):
		# Only include recognized attribute/values
		data = filter_unrecognized_keys(self.uris.keys(), data)
		# Ensure all attributes are present
		data = add_missing_keys(self.uris.keys(), data)
		return data

	def validate_resource(self, data):
		data = self.assign_preset_values(data)
		data = self.validate_attributes(data)
		data = self.validate_data(data)
		return data

	def validate_query(self, params):
		# Need to validate "list" type?
		params = self.assign_preset_values(params)
		params = self.validate_data(params)
		params = noneify_empty_dictionary_lists(params)
		return params