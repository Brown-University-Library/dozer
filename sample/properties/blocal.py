from dozer.graphschema import Domain


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

hasTeacher                 =  Domain(ns + 'hasTeacher',                 'uri')
netId                      =  Domain(ns + 'netId',                      'string')
geographicResearchAreaOf   =  Domain(ns + 'geographicResearchAreaOf',   'uri')
awardsAndHonors            =  Domain(ns + 'awardsAndHonors',            'string')
scholarlyWork              =  Domain(ns + 'scholarlyWork',              'string')
pubmedFirstName            =  Domain(ns + 'pubmedFirstName',            'string')
affiliations               =  Domain(ns + 'affiliations',               'string')
drrbWebPageOf              =  Domain(ns + 'drrbWebPageOf',              'uri')
shortId                    =  Domain(ns + 'shortId',                    'string')
hasAffiliation             =  Domain(ns + 'hasAffiliation',             'uri')
wikidataID                 =  Domain(ns + 'wikidataID',                 'string')
hasGeographicResearchArea  =  Domain(ns + 'hasGeographicResearchArea',  'uri')
fisCreated                 =  Domain(ns + 'fisCreated',                 'date')
orgUnit                    =  Domain(ns + 'orgUnit',                    'string')
degreeDate                 =  Domain(ns + 'degreeDate',                 'gYear')
drrbWebPage                =  Domain(ns + 'drrbWebPage',                'uri')
previousImage              =  Domain(ns + 'previousImage',              'uri')
researchStatement          =  Domain(ns + 'researchStatement',          'string')
delegateFor                =  Domain(ns + 'delegateFor',                'uri')
primaryOrgLabel            =  Domain(ns + 'primaryOrgLabel',            'string')
hasDelegate                =  Domain(ns + 'hasDelegate',                'uri')
fundedResearch             =  Domain(ns + 'fundedResearch',             'string')
countryCode                =  Domain(ns + 'countryCode',                'string')
fisUpdated                 =  Domain(ns + 'fisUpdated',                 'date')
teacherFor                 =  Domain(ns + 'teacherFor',                 'uri')
cvOf                       =  Domain(ns + 'cvOf',                       'uri')
profileUpdated             =  Domain(ns + 'profileUpdated',             'string')
pubmedLastName             =  Domain(ns + 'pubmedLastName',             'string')
cv                         =  Domain(ns + 'cv',                         'uri')
