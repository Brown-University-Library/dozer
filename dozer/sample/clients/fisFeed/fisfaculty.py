import requests

### start sketch
def build_queue(fis_list):
	all_faculty = requests.get(feed_base + "faculty")
	to_be_updated = [f for f in fis_list if f in all_faculty]
	to_be_created = [f for f in fis_list if f not in all_faculty]
	to_be_hidden = [f for f in all_faculty if f not in fis_list]
	return to_be_created, to_be_updated, to_be_hidden

def create(new_faculty_data):
	r = requests.post(feed_base + "faculty", data=new_faculty_data)

# https://tools.ietf.org/html/rfc6902#section-4.2
# http://jsonpatch.com/
# http://williamdurand.fr/2014/02/14/please-do-not-patch-like-an-idiot/

def update(upd_faculty_row):
	rabid = upd_faculty_row['resource_id']
	rsp = requests.get(feed_base + "faculty/" + rabid)
	if rsp:
		req = rsp.update(upd_faculty_row)
	r = requests.put(feed_base + "faculty/" + rabid, data=req)

def hide(hdn_faculty):
	rabid = hdn_faculty_row['resource_id']
	h_data = 	{
				'op': 'remove',
				'path': 'rdf:type',
				'value': blocal+'BrownThing'
				}
	r = requests.patch(feed_base + "faculty/" + rabid, data=h_data)

def process(fis_data):
	fis_list = cleanup(fis_data)
	crt, upd, hdn = build_queue(fis_list)
	for c in crt:
		create(c)
	for u in upd:
		update(u)
	for h in hdn:
		hide(h)

def update(shortId, atts):
	fac = Faculty.find_or_create(rabid=shortId)
	success = fac.update_attr(fis_data)
	if success:
		logging.info("Updated {0}: {1}").format(shortId, atts)
	else:
		logging.warning("Update failed for {0}: {1}").format(shortId, atts)
### end sketch