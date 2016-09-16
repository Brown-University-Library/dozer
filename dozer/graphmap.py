import os
import uuid


class Collection(object):
	def __init__(self, name, schema, named_graph, namespace, prefix):
		self.name = name
		self.schema = schema
		self.named_graph = named_graph
		self.namespace = namespace
		self.prefix = prefix

	def register_endpoint(self, endpoint):
		self.endpoint = endpoint

	def mint_new_uri(self):
		#does a prefix for resource hash even make sense?
		data_hash = self.resource_hash(self.prefix)
		return self.namespace_uri(data_hash)

	def resource_hash(self, prefix):
		return uuid.uuid4().hex

	def namespace_uri(self, suffix):
		return os.path.join(self.namespace, suffix)

	def create(self, data=dict(), aliased=False):
		uri = self.mint_new_uri()
		if aliased:
			data = self.schema.unalias_data(data)
		res = Resource(collection=self, uri=uri, incoming=data)
		resp = self.endpoint.update(insert=res)
		return resp

	def search(self, params=dict(), aliased=True):
		## IMPORTANT
		## should not be able to search on an optional term
		## or perhaps, not without required term present
		## leads to SPARQL weirdness
		## ALSO
		## lack of attribute validation can introduce issues
		if aliased:
			params = self.schema.unalias_data(params)
		query = Resource(collection=self, query=params)
		resp = self.endpoint.construct(query, optional=False)
		resList = [ Resource(uri=data.keys()[0],
					collection=self, searched=data.values()[0])
					for data in resp ]
		return resList

	def find(self, rabid):
		uri = self.namespace_uri(rabid)
		query = Resource(uri=uri, collection=self, query={})
		resp = self.endpoint.construct(query)
		resList = [ Resource(uri=data.keys()[0],
					collection=self, found=data.values()[0])
					for data in resp ]
		# Validate len(resList) == 1 ?
		return resList[0]

	def overwrite(self, existing, data, aliased=True):
		uri, data = data.items()[0]
		assert uri == existing.uri
		if aliased:
			data = self.schema.unalias_data(data)
		pending = Resource(
					uri=existing.uri, collection=self, incoming=data)
		resp = self.endpoint.update(insert=pending, delete=existing)
		return resp

	def modify(self, existing, data, aliased=True):
		uri, data = data.items()[0]
		assert uri == existing.uri
		if aliased:
			data = self.schema.unalias_data(data)
		uri, existing_data = existing.to_dict(alias=False).items()[0]
		pending = Resource(uri=existing.uri,
							collection=self, stored=existing_data)
		pending.update(data, validate_partial=True)
		resp = self.endpoint.update(insert=pending, delete=existing)
		return resp

	def remove(self, existing):
		resp = self.endpoint.update(delete=existing)
		return resp

class Resource(object):
	def __init__(self, collection, uri=None,
					incoming=None, query=None,
					searched=None, found=None):
		self.data = dict()
		self.collection = collection
		self.schema = collection.schema
		self.uri = uri
		if isinstance(incoming, dict):
			self.update(incoming, validate_raw=True)
		elif isinstance(searched, dict):
			self.update(searched)
		elif isinstance(found, dict):
			self.update(found, validate_stored=True)
		elif isinstance(query, dict):
			self.update(query, validate_query=True)

	def to_triples(self):
		return [(self.uri, k, val) for k,v in self.data.items()
					for val in v ]

	def to_dict(self, alias=True):
		if alias:
			data = self.schema.alias_data(self.data)
		else:
			data = self.data
		out = { self.uri: data }
		return out

	def update(self, data,
				validate_raw=False,
				validate_stored=False,
				validate_query=False):
		if validate_raw:
			data = self.schema.conform_structure(data)
			data = self.schema.conform_data(data)
			data = self.schema.validate_attributes(data)
			data = self.schema.validate_data(data)
		if validate_stored:
			data = self.schema.conform_data(data)
		if validate_query:
			data = self.schema.conform_structure(data)
			data = self.schema.conform_data(data)
			data = { k: v if v else [None] for k,v in data.items() }
		self.data.update(data)