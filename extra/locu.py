

import json
import urllib2
"""
api_key = '41b2c48a9bcf2fb82ae375fb88b474b3ee515871'

obj_json = json.load(urllib2.urlopen("https://api.locu.com/v1_0/venue/search/?country=india&region=New%20Delhi&api_key=41b2c48a9bcf2fb82ae375fb88b474b3ee515871"))

#print obj_json["objects"]

for item in obj_json["objects"]:
	#print "item is" + str(item)
	print item["name"]
	"""


def api_fun(query):

	api_key = '41b2c48a9bcf2fb82ae375fb88b474b3ee515871'
	url = 'https://api.locu.com/v1_0/venue/search/?api_key='
	query = query.replace(" ", "%20")
	final_url = url + api_key + "&locality="+ query +"&category=restaurant"

	var = json.load(urllib2.urlopen(final_url))

	for item in var['objects']:
		print "Name is:" + str(item["name"])
		print "# is" + str(item["phone"])


print(api_fun("New York")	)	 