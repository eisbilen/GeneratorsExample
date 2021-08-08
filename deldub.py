import json
import sys
from collections import OrderedDict
import csv
import os

jsonFile="/Users/erdemisbilen/Angular/TRTWorld/sport_article_links.json"

with open(jsonFile) as json_file:

	data = json.load(json_file)

	seen = OrderedDict()
	dubs = OrderedDict()

	for d in data:
		oid = d["article_url"]

		
		if oid not in seen:
			seen[oid] = d	
			
		else:
			dubs[oid]=d

	baseFileName=os.path.splitext(jsonFile)[0]

	with open('/Users/erdemisbilen/Angular/TRTWorld/sport_article_links_final.json', 'w') as out:
		json.dump(list(seen.values()), out)

	with open('/Users/erdemisbilen/Angular/TRTWorld/sport_article_links_deleted.json', 'w') as out:
		json.dump(list(dubs.values()), out)