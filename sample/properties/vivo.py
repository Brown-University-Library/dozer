from dozer.graphschema import Predicate


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

researchOverview         =  Predicate(ns + 'researchOverview',         'string')
positionInOrganization   =  Predicate(ns + 'positionInOrganization',   'uri')
positionForPerson        =  Predicate(ns + 'positionForPerson',        'uri')
middleName               =  Predicate(ns + 'middleName',               'string')
dateTimeInterval         =  Predicate(ns + 'dateTimeInterval',         'uri')
subOrganizationWithin    =  Predicate(ns + 'subOrganizationWithin',    'uri')
start                    =  Predicate(ns + 'start',                    'uri')
end                      =  Predicate(ns + 'end',                      'uri')
organizationForTraining  =  Predicate(ns + 'organizationForTraining',  'uri')
dateTimePrecision        =  Predicate(ns + 'dateTimePrecision',        'uri')
hasSubOrganization       =  Predicate(ns + 'hasSubOrganization',       'uri')
linkAnchorText           =  Predicate(ns + 'linkAnchorText',           'string')
teachingOverview         =  Predicate(ns + 'teachingOverview',         'string')
trainingAtOrganization   =  Predicate(ns + 'trainingAtOrganization',   'uri')
hasResearchArea          =  Predicate(ns + 'hasResearchArea',          'uri')
overview                 =  Predicate(ns + 'overview',                 'string')
personInPosition         =  Predicate(ns + 'personInPosition',         'uri')
webpageOf                =  Predicate(ns + 'webpageOf',                'uri')
organizationForPosition  =  Predicate(ns + 'organizationForPosition',  'uri')
hasCollaborator          =  Predicate(ns + 'hasCollaborator',          'uri')
webpage                  =  Predicate(ns + 'webpage',                  'uri')
rank                     =  Predicate(ns + 'rank',                     'int')
primaryEmail             =  Predicate(ns + 'primaryEmail',             'string')
preferredTitle           =  Predicate(ns + 'preferredTitle',           'string')
linkURI                  =  Predicate(ns + 'linkURI',                  'string')
dateTime                 =  Predicate(ns + 'dateTime',                 'dateTime')
educationalTrainingOf    =  Predicate(ns + 'educationalTrainingOf',    'uri')
educationalTraining      =  Predicate(ns + 'educationalTraining',      'uri')
researchAreaOf           =  Predicate(ns + 'researchAreaOf',           'uri')
