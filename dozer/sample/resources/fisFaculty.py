from graphschema import Schema, Attribute
from graphmap import Collection
from sample.properties import foaf, vivo, blocal, rdfs, rdf, bdisplay

#rename presets as only; add parameter for allowed
fisFacultySchema = Schema({
	'class'		: 	Attribute(rdf.rdfType, required=True,
						always=[ vivo.FacultyMember ],
						allowed=[	vivo.FacultyMember,
									blocal.BrownThing,
									bdisplay.Hidden ]),
	'label'		:	Attribute(rdfs.label, required=True, unique=True),
	'first'		:	Attribute(foaf.firstName, required=True, unique=True),
	'last'		:	Attribute(foaf.lastName, required=True, unique=True),
	'title'		:	Attribute(vivo.preferredTitle, required=True, unique=True),
	'email'		:	Attribute(vivo.primaryEmail, required=True, unique=True),
	'shortid'	: 	Attribute(blocal.shortId, required=True, unique=True),
	'middle'	:	Attribute(vivo.middleName, optional=True, unique=True),
	'updated'	: 	Attribute(blocal.fisUpdated, optional=True),
	'created'	:	Attribute(blocal.fisCreated, optional=True),
	'primaryou'	: 	Attribute(blocal.primaryOrgLabel, optional=True),
})

# rename namespace; "resource namespace"?
fisFaculty = Collection(
				name='fisFaculty',
				schema=fisFacultySchema,
				named_graph='http://vitro.mannlib.cornell.edu/default/vitro-kb-2',
				namespace='http://vivo.brown.edu/individual/',
				prefix='faculty')