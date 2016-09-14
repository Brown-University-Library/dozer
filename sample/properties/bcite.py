from statements import Predicate


### Model Namespace ###

ns =  'http://vivo.brown.edu/ontology/citation#'

### Class Declarations ###

Citation            =  ns + 'Citation'
Review              =  ns + 'Review'
Abstract            =  ns + 'Abstract'
Article             =  ns + 'Article'
Contributor         =  ns + 'Contributor'
Conference          =  ns + 'Conference'
Publisher           =  ns + 'Publisher'
Location            =  ns + 'Location'
ConferencePaper     =  ns + 'ConferencePaper'
Book                =  ns + 'Book'
Chapter             =  ns + 'Chapter'
Venue               =  ns + 'Venue'
ConferenceLocation  =  ns + 'ConferenceLocation'
BookSection         =  ns + 'BookSection'
Patent              =  ns + 'Patent'
WorkingPaper        =  ns + 'WorkingPaper'

### Property Declarations ###

contributorTo          =  Predicate(ns + 'contributorTo',          'uri')
conferenceDate         =  Predicate(ns + 'conferenceDate',         'dateTime')
authorList             =  Predicate(ns + 'authorList',             'string')
title                  =  Predicate(ns + 'title',                  'string')
doi                    =  Predicate(ns + 'doi',                    'string')
issn                   =  Predicate(ns + 'issn',                   'string')
book                   =  Predicate(ns + 'book',                   'string')
hasVenue               =  Predicate(ns + 'hasVenue',               'uri')
url                    =  Predicate(ns + 'url',                    'string')
hasConferenceLocation  =  Predicate(ns + 'hasConferenceLocation',  'uri')
editorList             =  Predicate(ns + 'editorList',             'string')
version                =  Predicate(ns + 'version',                'string')
cvId                   =  Predicate(ns + 'cvId',                   'string')
cites                  =  Predicate(ns + 'cites',                  'uri')
wokId                  =  Predicate(ns + 'wokId',                  'string')
pageStart              =  Predicate(ns + 'pageStart',              'string')
hasPublisher           =  Predicate(ns + 'hasPublisher',           'uri')
hasLocation            =  Predicate(ns + 'hasLocation',            'uri')
issue                  =  Predicate(ns + 'issue',                  'string')
pageEnd                =  Predicate(ns + 'pageEnd',                'string')
firstName              =  Predicate(ns + 'firstName',              'string')
locationFor            =  Predicate(ns + 'locationFor',            'uri')
conferenceLocationFor  =  Predicate(ns + 'conferenceLocationFor',  'uri')
middleName             =  Predicate(ns + 'middleName',             'string')
isbn                   =  Predicate(ns + 'isbn',                   'string')
oclc                   =  Predicate(ns + 'oclc',                   'string')
lastName               =  Predicate(ns + 'lastName',               'string')
pmid                   =  Predicate(ns + 'pmid',                   'string')
citedAs                =  Predicate(ns + 'citedAs',                'uri')
volume                 =  Predicate(ns + 'volume',                 'string')
number                 =  Predicate(ns + 'number',                 'string')
hasContributor         =  Predicate(ns + 'hasContributor',         'uri')
pages                  =  Predicate(ns + 'pages',                  'string')
venueFor               =  Predicate(ns + 'venueFor',               'uri')
hasConference          =  Predicate(ns + 'hasConference',          'uri')
date                   =  Predicate(ns + 'date',                   'dateTime')
pmcid                  =  Predicate(ns + 'pmcid',                  'string')
publisherFor           =  Predicate(ns + 'publisherFor',           'uri')
conferenceFor          =  Predicate(ns + 'conferenceFor',          'uri')
