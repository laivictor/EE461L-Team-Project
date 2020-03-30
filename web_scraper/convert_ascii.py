import json

with open('web_scraper/countries.json') as f:
	d = json.load(f)

with open('countries.json', 'w') as out:
	json.dump(d, out, ensure_ascii = False, indent = 2)