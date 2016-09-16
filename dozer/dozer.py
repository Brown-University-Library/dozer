#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
from flask.ext.cors import CORS
import json

app = Flask(__name__)
CORS(app)

from sparqler import Sparqler

spq = Sparqler(
		'http://localhost:8082/VIVO/query',
		'http://localhost:8080/rab/api/sparqlUpdate',
		'http')

## API for FIS faculty data
from sample.resources.fisFaculty import fisFaculty
fisFaculty.register_endpoint(spq)

@app.route('/rabdata/fisfeed/faculty/', methods=['GET'])
def index():
	# Working for single strings
	# problems for dates, multival?
	params = { k: [v] for k, v in request.args.items() }
	try:
		allFisFaculty = fisFaculty.search(params=params)
	except:
		return 404
	return json.dumps([ fac.to_dict()
							for fac in allFisFaculty])

@app.route('/rabdata/fisfeed/faculty/<rabid>', methods=['GET'])
def retrieve(rabid):
	try:
		fisfac = fisFaculty.find(rabid=rabid)
	except:
		return 404
	return json.dumps(fisfac.to_dict())


@app.route('/rabdata/fisfeed/faculty/', methods=['POST'])
def create():
	try:
		new = fisFaculty.create(json.loads(resp.body))
	except:
		return 400
	return response(code=201, body=new)


@app.route('/rabdata/fisfeed/faculty/<rabid>', methods=['PUT'])
def replace(rabid):
	try:
		fisfac = fisFaculty.find(rabid=rabid)
	except:
		return 404
	if fisfac.ETag == req.headers["If-Match"]:
		try:
			updated = fisFaculty.overwrite(fisfac, json.loads(req.body))
		except:
			return 400
		return response(code=201, body=updated)
	else:
		return 409


@app.route('/rabdata/fisfeed/faculty/<rabid>', methods=['DELETE'])
def destroy(rabid):
	try:
		fisfac = fisFaculty.find(rabid=rabid)
	except:
		return 404
	if fisfac.ETag == req.headers["If-Match"]:
		try:
			fisfac.remove()
		except:
			return 403
		return 204
	else:
		return 409

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, debug=True)