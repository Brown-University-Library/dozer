from dozer.graphschema import Predicate


### Model Namespace ###

ns =  'http://vivo.brown.edu/ontology/vivo-brown/'

### Class Declarations ###

Delegate                =  ns + 'Delegate'
Country                 =  ns + 'Country'
ClinicalDepartment      =  ns + 'ClinicalDepartment'
InstituteCenterProgram  =  ns + 'InstituteCenterProgram'
BrownThing              =  ns + 'BrownThing'
Place                   =  ns + 'Place'
ResearchArea            =  ns + 'ResearchArea'
CV                      =  ns + 'CV'

### Property Declarations ###

hasTeacher                 =  Predicate(ns + 'hasTeacher',                 'uri')
netId                      =  Predicate(ns + 'netId',                      'string')
geographicResearchAreaOf   =  Predicate(ns + 'geographicResearchAreaOf',   'uri')
awardsAndHonors            =  Predicate(ns + 'awardsAndHonors',            'string')
scholarlyWork              =  Predicate(ns + 'scholarlyWork',              'string')
pubmedFirstName            =  Predicate(ns + 'pubmedFirstName',            'string')
affiliations               =  Predicate(ns + 'affiliations',               'string')
drrbWebPageOf              =  Predicate(ns + 'drrbWebPageOf',              'uri')
shortId                    =  Predicate(ns + 'shortId',                    'string')
hasAffiliation             =  Predicate(ns + 'hasAffiliation',             'uri')
wikidataID                 =  Predicate(ns + 'wikidataID',                 'string')
hasGeographicResearchArea  =  Predicate(ns + 'hasGeographicResearchArea',  'uri')
fisCreated                 =  Predicate(ns + 'fisCreated',                 'date')
orgUnit                    =  Predicate(ns + 'orgUnit',                    'string')
degreeDate                 =  Predicate(ns + 'degreeDate',                 'gYear')
drrbWebPage                =  Predicate(ns + 'drrbWebPage',                'uri')
previousImage              =  Predicate(ns + 'previousImage',              'uri')
researchStatement          =  Predicate(ns + 'researchStatement',          'string')
delegateFor                =  Predicate(ns + 'delegateFor',                'uri')
primaryOrgLabel            =  Predicate(ns + 'primaryOrgLabel',            'string')
hasDelegate                =  Predicate(ns + 'hasDelegate',                'uri')
fundedResearch             =  Predicate(ns + 'fundedResearch',             'string')
countryCode                =  Predicate(ns + 'countryCode',                'string')
fisUpdated                 =  Predicate(ns + 'fisUpdated',                 'date')
teacherFor                 =  Predicate(ns + 'teacherFor',                 'uri')
cvOf                       =  Predicate(ns + 'cvOf',                       'uri')
profileUpdated             =  Predicate(ns + 'profileUpdated',             'string')
pubmedLastName             =  Predicate(ns + 'pubmedLastName',             'string')
cv                         =  Predicate(ns + 'cv',                         'uri')
