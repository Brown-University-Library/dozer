from statements import Predicate

ns = 'http://www.w3.org/2004/02/skos/core#'

broader = Predicate(ns + 'broader', 'uri')
narrower = Predicate(ns + 'narrower', 'uri')
related = Predicate(ns + 'related', 'uri')
prefLabel = Predicate(ns + 'prefLabel', 'string')
altLabel = Predicate(ns + 'altLabel', 'string')
hiddenLabel = Predicate(ns + 'hiddenLabel', 'string')