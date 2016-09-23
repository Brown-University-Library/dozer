import datetime
import urlparse

#####################
## Begin Domain #####
#####################

def _validate_uri(value):
	try:
		parsed = urlparse.urlparse(value)
		assert parsed.scheme
		assert parsed.netloc
	except:
		raise ValueError("Bad URI: " + value)
	return value

def _validate_int(value):
	if isinstance(value, int):
		return value
	else:
		raise ValueError("Bad int: " + value)

def _validate_datetime(value):
	try:
		datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')
	except:	
		raise ValueError("Bad date: " + value)
	return value

def _validate_string(value):
	try:
		value.decode('UTF-8')
	except:
		raise UnicodeError("Bad unicode: " + value)
	return value

class Domain(object):

	def __init__(self, uri, datatype):
		self.uri = _validate_uri(uri)
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
		elif datatype == 'year' or datatype == 'gYear':
			pass
		else:
			raise ValueError("Unknown datatype: " + datatype)

	def validate(self, value):
		return self.validator(value)

###################
## End Domain #####
###################

#####################
## Begin Attribute ##
#####################

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
	def __init__(self, domain, alias=None,
					required=False, optional=False,
					unique=False, allowed=None,
					always=None, only=None):
		self.domain = domain
		self.uri = domain.uri
		self.alias = alias
		self.validators = []
		self.conformers = []
		if required:
			self.required = True
			self.validators.append(_validate_required)
		if unique:
			self.unique = True
			self.validators.append(_validate_unique)
		if always:
			assert isinstance(always, list)
			self.always = always
			self.validators.append(self._validate_always)
			self.conformers.append(self._conform_always)
		if allowed:
			assert isinstance(allowed, list)
			self.allowed = allowed
			self.validators.append(self._validate_allowed)
			self.conformers.append(self._conform_allowed)
		if only:
			assert isinstance(only, list)
			self.only = only
			self.validators.append(self._validate_only)
			self.conformers.append(self._conform_only)

	def set_alias(self, alias):
		self.alias = alias

	def _validate_always(self, values):
		for always in self.always:
			try:
				assert always in values
			except:
				raise Exception(always)
		return values

	def _validate_allowed(self, values):
		for value in values:
			try:
				assert value in self.allowed
			except:
				raise Exception(self.allowed)
		return values

	def _validate_only(self, values):
		for only in self.only:
			try:
				assert only in values
			except:
				raise Exception(self.only)
		for value in values:
			try:
				assert value in self.only
			except:
				raise Exception(self.only)
		return values

	def _conform_always(self, values):
		return list(set(self.always) | set(values))

	def _conform_allowed(self, values):
		return list(set(self.allowed) & set(values))

	def _conform_only(self, values):
		return self.only

###################
## End Attribute ##
###################

##################
## Begin Schema ##
##################

def _validate_map(dct):
	try:
		assert isinstance(dct, dict)
	except:
		raise ValueError(dct)
	return dct

def _validate_fields(dct, keyList):
	try:
		assert set(dct.keys()) == set(keyList)
	except:
		raise ValueError(set(dct.keys()) ^ set(keyList))
	return dct

def _validate_map_arrays(dct):
	for k, v in dct.items():
		try:
			assert isinstance(v, list)
		except:
			raise ValueError(k)
	return dct		

def attribute_builder(aliasDict):
	for alias in aliasDict:
		aliasDict[alias].set_alias(alias)
	return [ attr for attr in aliasDict.values() ]

class Schema(object):
	def __init__(self, attrs):
		if isinstance(attrs, dict):
			attrs = attribute_builder(attrs)
		self._attrs = attrs
		self.attributes = [ attr.uri for attr in attrs ]
		self.labels = { attr.alias: attr.uri for attr in attrs }
		self.attr_validators = { attr.uri: attr.validators for attr in attrs }
		self.data_validators = { attr.uri: attr.domain.validator for attr in attrs }
		self.data_conformers = { attr.uri: attr.conformers for attr in attrs}				
		self.required = [ attr.uri for attr in attrs if hasattr(attr,'required') ]
		self.optional = [ attr.uri for attr in attrs if not hasattr(attr,'required') ]
		self.datatypes = { attr.uri: attr.domain.datatype for attr in attrs }

	def conform_data(self, data):
		out = dict()
		for k, v in data.items():
			conformers = self.data_conformers[k]
			filtered = v
			for conformer in conformers:
				try:
					filtered = conformer(filtered)
				except ValueError as e:
					raise Exception(e,k,v)
			out[k] = filtered
		return out

	def validate_structure(self, data):
		data = _validate_map(data)
		data = _validate_fields(data, self.attributes)
		data = _validate_map_arrays(data)
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

################
## End Schema ##
################