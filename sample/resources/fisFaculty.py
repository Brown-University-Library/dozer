import os

from dozer.graphschema import Schema, Attribute
from dozer.graphmap import Collection
from dozer.sparqler import Sparqler

from properties import foaf, vivo, blocal, rdfs, rdf, bdisplay


query_api = os.environ['QUERY_URL']
update_api = os.environ['UPDATE_URL']
user_email = os.environ['UPDATE_EMAIL']
user_pass = os.environ['UPDATE_PASS']

spq = Sparqler( query_api, update_api,
				user_email, user_pass, 'http')

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
				named_graph='http://vivo.brown.edu/data/fis-faculty',
				namespace='http://vivo.brown.edu/individual/',
				prefix='faculty')
fisFaculty.register_endpoint(spq)