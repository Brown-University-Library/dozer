from dozer.graphschema import Predicate


### Model Namespace ###

ns =  'http://xmlns.com/foaf/0.1/'

### Class Declarations ###

Person        =  ns + 'Person'
Organization  =  ns + 'Organization'
Agent         =  ns + 'Agent'

### Property Declarations ###

firstName  =  Predicate(ns + 'firstName',  'string')
lastName   =  Predicate(ns + 'lastName',   'string')
