import sys
import os

import xml.etree.ElementTree as ET

xsd_ns = "http://www.w3.org/2001/XMLSchema#"
owl_ns = "http://www.w3.org/2002/07/owl#"

owl_class = "http://www.w3.org/2002/07/owl#Class" 
object_property = "http://www.w3.org/2002/07/owl#ObjectProperty"
data_property = "http://www.w3.org/2002/07/owl#DatatypeProperty"

def extract_label(uri, namespace):
	assert namespace in uri
	label = uri[len(namespace):]
	return label

def main(modelDir, modelFile, propDir):

	## Build document tree
	tree = ET.parse(modelDir+modelFile)
	root = tree.getroot()
	## end Build document tree


	## Iterate over tree and acquire URIs
	ont_classes = []
	ont_properties = []
	for desc in root:
		types = desc.findall(
					"{http://www.w3.org/1999/02/22-rdf-syntax-ns#}type")
		type_uris = [ t.get(
						"{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource")
							for t in types ]
		if owl_class in type_uris:
			uri = desc.get(
					"{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about")
			ont_classes.append(uri)
		elif object_property in type_uris:
			uri = desc.get(
					"{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about")
			ont_properties.append((uri,'uri'))
		elif data_property in type_uris:
			uri = desc.get(
					"{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about")
			range_elem = desc.find(
				"{http://www.w3.org/2000/01/rdf-schema#}range")
			if range_elem is not None:
				nsd_range = range_elem.get(
					"{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource")
				dt_range = extract_label(nsd_range, xsd_ns)
			else:
				dt_range = 'string'
			ont_properties.append((uri,dt_range))
	## end Iterate over tree and acquire URIs

	## Finding the namespace
	if ont_classes:
		check = ont_classes[0]
	elif ont_properties:
		check = ont_properties[0]
	else:
		raise "No data to parse"
	try:
		delim = check.rindex('#')
	except ValueError:
		delim = check.rindex('/')
	except ValueError:
		raise Exception("Namespace not found")
	except:
		raise
	namespace = check[:delim+1]
	## end Finding the namespace

	## Vars for pretty printing
	outfile = modelFile[:-3] + 'py'
	prop_uris = [p[0] for p in ont_properties]
	pp_class = len(max(ont_classes, key=len)) - len(namespace) + 2
	pp_prop = len(max(prop_uris, key=len)) - len(namespace) + 2
	## end Vars for pretty printing

	## Building the file string
	out = "from dozer.statements import Predicate\n\n"
	out += "\n### Model Namespace ###\n\n"
	out += "ns =  '{0}'\n".format(namespace)
	out += "\n### Class Declarations ###\n\n"
	for c in ont_classes:
		text = extract_label(c,namespace)
		out += "{0}{1}=  ns + '{0}'\n".format(text, ' '*(pp_class - len(text)))
	out += "\n### Property Declarations ###\n\n"
	for p in ont_properties:
		text = extract_label(p[0], namespace)
		out += "{0}{2}=  Predicate(ns + '{0}',{2}'{1}')\n".format(
											text,p[1],' '*(pp_prop - len(text)))
	## end Building the file string

	## Write the file
	with open(propDir+outfile, 'w') as f:
		f.write(out)
	## end Write the file 

if __name__ == "__main__":

	## Expects as arguments:
	## 1: a directory holding RDF/XML ontology files
	## files *MUST* have extension /.xml/
	## 2: a directory to write to 
	model_dir = sys.argv[1]
	prop_dir = sys.argv[2]

	## List ontology files from model_dir
	model_files = []
	for (model_path, _, model_file) in os.walk(model_dir):
		model_files.extend(model_file)
	## end List ontology files from model_dir

	## Run script for each model file
	for mfile in model_files:
		main(model_dir, mfile, prop_dir)
	## end Run script for each model file