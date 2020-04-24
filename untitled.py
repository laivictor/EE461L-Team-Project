import countrydb

countries = countrydb.get_all_countries()

for i in countries:
	print(i['img'])
	print(type(i['img']))
