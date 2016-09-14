from dozer.statements import Collection, Schema, Attribute
from ..properties import foaf, vivo, blocal, rdfs, rdf

#rename presets as only; add parameter for allowed
fisFacultySchema = Schema({
	'class'			: 	Attribute(rdf.rdfType, required=True,
							presets=[
								'http://vivoweb.org/ontology/core#FacultyMember',
								'http://vivo.brown.edu/ontology/vivo-brown/BrownThing'
							]),
	'label'			:	Attribute(rdfs.label, required=True, unique=True),
	'first'			:	Attribute(foaf.firstName, required=True, unique=True),
	'last'			:	Attribute(foaf.lastName, required=True, unique=True),
	'title'			:	Attribute(vivo.preferredTitle, required=True, unique=True),
	'email'			:	Attribute(vivo.primaryEmail, required=True, unique=True),
	'short_id'		: 	Attribute(blocal.shortId, required=True),
	'updated_date'	: 	Attribute(blocal.fisUpdated, optional=True),
	'primary_ou'	: 	Attribute(blocal.primaryOrgLabel, optional=True),
})

# rename namespace; "resource namespace"?
fisFaculty = Collection(
				name='fisFaculty',
				schema=fisFacultySchema,
				named_graph='http://vitro.mannlib.cornell.edu/default/vitro-kb-2',
				namespace='http://vivo.brown.edu/individual/',
				prefix='faculty')