from graphschema import ValidationError
from graphmap import AliasError

# http://flask.pocoo.org/docs/0.11/patterns/apierrors/
class RESTError(Exception):
    status_code = 400
    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = { 'context': payload }

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv