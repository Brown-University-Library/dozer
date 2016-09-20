from graphschema import Predicate


### Model Namespace ###

ns =  'http://vivo.brown.edu/ontology/profile#'

### Class Declarations ###

HospitalAppointment  =  ns + 'HospitalAppointment'
PostdocAppointment   =  ns + 'PostdocAppointment'
Certification        =  ns + 'Certification'
Certifier            =  ns + 'Certifier'
Credential           =  ns + 'Credential'
Specialty            =  ns + 'Specialty'
License              =  ns + 'License'
Hospital             =  ns + 'Hospital'
Licensor             =  ns + 'Licensor'
Accreditor           =  ns + 'Accreditor'
Training             =  ns + 'Training'
Appointment          =  ns + 'Appointment'

### Property Declarations ###

hasHospital          =  Predicate(ns + 'hasHospital',          'uri')
hasAppointment       =  Predicate(ns + 'hasAppointment',       'uri')
hasTraining          =  Predicate(ns + 'hasTraining',          'uri')
appointmentFor       =  Predicate(ns + 'appointmentFor',       'uri')
department           =  Predicate(ns + 'department',           'string')
state                =  Predicate(ns + 'state',                'string')
country              =  Predicate(ns + 'country',              'string')
hasCredential        =  Predicate(ns + 'hasCredential',        'uri')
specialtyFor         =  Predicate(ns + 'specialtyFor',         'uri')
credentialGrantedBy  =  Predicate(ns + 'credentialGrantedBy',  'uri')
hasOrganization      =  Predicate(ns + 'hasOrganization',      'uri')
city                 =  Predicate(ns + 'city',                 'string')
credentialFor        =  Predicate(ns + 'credentialFor',        'uri')
organizationFor      =  Predicate(ns + 'organizationFor',      'uri')
grantsCredential     =  Predicate(ns + 'grantsCredential',     'uri')
endDate              =  Predicate(ns + 'endDate',              'dateTime')
credentialNumber     =  Predicate(ns + 'credentialNumber',     'string')
hasSpecialty         =  Predicate(ns + 'hasSpecialty',         'uri')
trainingFor          =  Predicate(ns + 'trainingFor',          'uri')
startDate            =  Predicate(ns + 'startDate',            'dateTime')
hospitalFor          =  Predicate(ns + 'hospitalFor',          'uri')
