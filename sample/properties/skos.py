from graphschema import Domain


### Model Namespace ###

ns =  'http://www.w3.org/2004/02/skos/core#'

### Class Declarations ###

Concept  =  ns + 'Concept'

### Property Declarations ###

exactMatch  =  Domain(ns + 'exactMatch',  'uri')
