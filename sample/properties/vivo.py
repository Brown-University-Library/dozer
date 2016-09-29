from dozer.graphschema import Domain


### Model Namespace ###

ns =  'http://vivoweb.org/ontology/core#'

### Class Declarations ###

University                     =  ns + 'University'
FacultyAdministrativePosition  =  ns + 'FacultyAdministrativePosition'
URLLink                        =  ns + 'URLLink'
Course                         =  ns + 'Course'
DateTimeValue                  =  ns + 'DateTimeValue'
AcademicTerm                   =  ns + 'AcademicTerm'
Division                       =  ns + 'Division'
EducationalTraining            =  ns + 'EducationalTraining'
FacultyPosition                =  ns + 'FacultyPosition'
FacultyMember                  =  ns + 'FacultyMember'
DateTimeInterval               =  ns + 'DateTimeInterval'
AcademicDepartment             =  ns + 'AcademicDepartment'
Department                     =  ns + 'Department'
Position                       =  ns + 'Position'

### Property Declarations ###

researchOverview         =  Domain(ns + 'researchOverview',         'string')
positionInOrganization   =  Domain(ns + 'positionInOrganization',   'uri')
positionForPerson        =  Domain(ns + 'positionForPerson',        'uri')
middleName               =  Domain(ns + 'middleName',               'string')
dateTimeInterval         =  Domain(ns + 'dateTimeInterval',         'uri')
subOrganizationWithin    =  Domain(ns + 'subOrganizationWithin',    'uri')
start                    =  Domain(ns + 'start',                    'uri')
end                      =  Domain(ns + 'end',                      'uri')
organizationForTraining  =  Domain(ns + 'organizationForTraining',  'uri')
dateTimePrecision        =  Domain(ns + 'dateTimePrecision',        'uri')
hasSubOrganization       =  Domain(ns + 'hasSubOrganization',       'uri')
linkAnchorText           =  Domain(ns + 'linkAnchorText',           'string')
teachingOverview         =  Domain(ns + 'teachingOverview',         'string')
trainingAtOrganization   =  Domain(ns + 'trainingAtOrganization',   'uri')
hasResearchArea          =  Domain(ns + 'hasResearchArea',          'uri')
overview                 =  Domain(ns + 'overview',                 'string')
personInPosition         =  Domain(ns + 'personInPosition',         'uri')
webpageOf                =  Domain(ns + 'webpageOf',                'uri')
organizationForPosition  =  Domain(ns + 'organizationForPosition',  'uri')
hasCollaborator          =  Domain(ns + 'hasCollaborator',          'uri')
webpage                  =  Domain(ns + 'webpage',                  'uri')
rank                     =  Domain(ns + 'rank',                     'int')
primaryEmail             =  Domain(ns + 'primaryEmail',             'string')
preferredTitle           =  Domain(ns + 'preferredTitle',           'string')
linkURI                  =  Domain(ns + 'linkURI',                  'string')
dateTime                 =  Domain(ns + 'dateTime',                 'dateTime')
educationalTrainingOf    =  Domain(ns + 'educationalTrainingOf',    'uri')
educationalTraining      =  Domain(ns + 'educationalTraining',      'uri')
researchAreaOf           =  Domain(ns + 'researchAreaOf',           'uri')
