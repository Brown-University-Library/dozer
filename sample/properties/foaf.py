from dozer.graphschema import Domain


### Model Namespace ###

ns =  'http://xmlns.com/foaf/0.1/'

### Class Declarations ###

Person        =  ns + 'Person'
Organization  =  ns + 'Organization'
Agent         =  ns + 'Agent'

### Property Declarations ###

firstName  =  Domain(ns + 'firstName',  'string')
lastName   =  Domain(ns + 'lastName',   'string')
