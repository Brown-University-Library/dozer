import sys
import xml.etree.ElementTree as ET

xsd_ns = "http://www.w3.org/2001/XMLSchema#"
owl_ns = "http://www.w3.org/2002/07/owl#"

owl_class = "http://www.w3.org/2002/07/owl#Class" 
object_property = "http://www.w3.org/2002/07/owl#ObjectProperty"
data_property = "http://www.w3.org/2002/07/owl#DatatypeProperty"

def extract_label(uri, namespace):
	label = uri[len(namespace):]
	return label

def main(ontologyFile, ontologyAbbv, namespace):
	outfile = ontologyAbbv + '.py'

	ppleft = 24

	out = "from statements import Predicate\n\n"
	out += "ns =  '{0}'\n\n".format(namespace)

	ont_classes = []
	ont_properties = []

	tree = ET.parse(ontologyFile)
	root = tree.getroot()
	for desc in root:
		types = desc.findall(
					"{http://www.w3.org/1999/02/22-rdf-syntax-ns#}type")
		type_uris = [ t.get(
						"{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource")
							for t in types ]
		if owl_class in type_uris:
			uri = desc.get(
					"{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about")
			ont_classes.append(extract_label(uri, namespace))
		elif object_property in type_uris:
			uri = desc.get(
					"{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about")
			ont_properties.append((extract_label(uri, namespace),'uri'))
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
			ont_properties.append((extract_label(uri, namespace),dt_range))

	for c in ont_classes:
		out += "{0}{1}=  ns + '{0}'\n".format(c, ' '*(ppleft - len(c)))
	out += "\n\n"
	for p in ont_properties:
		out += "{0}{2}=  Predicate(ns + '{0}', '{1}')\n".format(
											p[0],p[1],' '*(ppleft - len(p[0])))

	with open(outfile, 'w') as f:
		f.write(out)

if __name__ == "__main__":
	main(sys.argv[1],sys.argv[2],sys.argv[3])