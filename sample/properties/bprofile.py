from dozer.graphschema import Domain


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

hasHospital          =  Domain(ns + 'hasHospital',          'uri')
hasAppointment       =  Domain(ns + 'hasAppointment',       'uri')
hasTraining          =  Domain(ns + 'hasTraining',          'uri')
appointmentFor       =  Domain(ns + 'appointmentFor',       'uri')
department           =  Domain(ns + 'department',           'string')
state                =  Domain(ns + 'state',                'string')
country              =  Domain(ns + 'country',              'string')
hasCredential        =  Domain(ns + 'hasCredential',        'uri')
specialtyFor         =  Domain(ns + 'specialtyFor',         'uri')
credentialGrantedBy  =  Domain(ns + 'credentialGrantedBy',  'uri')
hasOrganization      =  Domain(ns + 'hasOrganization',      'uri')
city                 =  Domain(ns + 'city',                 'string')
credentialFor        =  Domain(ns + 'credentialFor',        'uri')
organizationFor      =  Domain(ns + 'organizationFor',      'uri')
grantsCredential     =  Domain(ns + 'grantsCredential',     'uri')
endDate              =  Domain(ns + 'endDate',              'dateTime')
credentialNumber     =  Domain(ns + 'credentialNumber',     'string')
hasSpecialty         =  Domain(ns + 'hasSpecialty',         'uri')
trainingFor          =  Domain(ns + 'trainingFor',          'uri')
startDate            =  Domain(ns + 'startDate',            'dateTime')
hospitalFor          =  Domain(ns + 'hospitalFor',          'uri')
