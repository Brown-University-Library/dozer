#!flask/bin/python
import context

from flask import Flask, jsonify, abort, request, make_response, url_for
from flask.ext.cors import CORS
import json

app = Flask(__name__)
CORS(app)

from resources.errors import ValidationError, \
	AliasError, RESTError

@app.errorhandler(RESTError)
def handle_rest_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


## API for FIS faculty data
from resources.fisFaculty import fisFaculty

@app.route('/rabdata/fisfaculty/', methods=['GET'])
def index():
	# Working for single strings
	# problems for dates, multival?
	params = { k: [v] for k, v in request.args.items() }
	try:
		allFisFaculty = fisFaculty.search(params=params)
	except AliasError as e:
		raise RESTError('Bad parameter',
			status_code=400, payload=e.msg)
	except:
		raise RESTError('Resource not found', status_code=404)
	return json.dumps([ fac.to_dict()
							for fac in allFisFaculty])

@app.route('/rabdata/fisfaculty/<rabid>', methods=['GET'])
def retrieve(rabid):
	try:
		fisfac = fisFaculty.find(rabid=rabid)
	except:
		raise RESTError('Resource not found', status_code=404)
	resp = make_response(
				json.dumps(fisfac.to_dict()))
	resp.headers['ETag'] = fisfac.etag
	return resp

@app.route('/rabdata/fisfaculty/', methods=['POST'])
def create():
	try:
		fisfac = fisFaculty.create(
					data=request.get_json())
	except (AliasError, ValidationError) as e:
		raise RESTError('Bad data',
					status_code=400, payload=e.msg) 
	resp = make_response(
				json.dumps(fisfac.to_dict()))
	resp.headers['ETag'] = fisfac.etag
	return resp

@app.route('/rabdata/fisfaculty/<rabid>', methods=['PUT'])
def replace(rabid):
	try:
		fisfac = fisFaculty.find(rabid=rabid)
	except:
		raise RESTError('Resource not found', status_code=404)
	if fisfac.etag == request.headers.get("If-Match"):
		try:
			updated = fisFaculty.overwrite(fisfac, request.get_json())
		except (AliasError, ValidationError) as e:
			raise RESTError('Validation',
				status_code=400, payload=e.msg)
		resp = make_response(
				json.dumps(updated.to_dict()))
		resp.headers['ETag'] = updated.etag
		return resp
	else:
		raise RESTError('Data modified on server',
							status_code=409, payload=fisfac.to_dict())

@app.route('/rabdata/fisfaculty/<rabid>', methods=['DELETE'])
def destroy(rabid):
	try:
		fisfac = fisFaculty.find(rabid=rabid)
	except:
		raise RESTError('No resource to delete', status_code=410)
	if fisfac.etag == request.headers.get("If-Match"):
		try:
			fisFaculty.remove(fisfac)
			resp = make_response('', 204)
			return resp
		except (AliasError, ValidationError) as e:
			raise RESTError('Validation',
				status_code=400, payload=e.msg)
	else:
		raise RESTError('Data modified on server',
							status_code=409, payload=fisfac.to_dict())

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, debug=True)