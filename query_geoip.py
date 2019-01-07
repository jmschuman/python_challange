

# "city":"Newark","country":"United States","countryCode":"US","lat":40.7357,"lon":-74.1724,"region":"NJ","regionName":"New Jersey","timezone":"America/New_York","zip":"07175"}

def query(opts, data):

	Options = ["City", "Country", "CountryCode", "Region", "RegionName", "Timezone", "Zip_code"]
	resulting_data = []

	for a,b in data.items():
		c = 0
		for o in opts:
			"""print(o)
												print(b)"""
			if o in Options:
				"""print(b[Options.index(o)])
																print("||")
																print(str(opts[o]))"""
				if str(b[Options.index(o)]) == str(opts[o]):
					c += 1
		if c == len(list(opts)):
			resulting_data.append(a)

	if len(resulting_data) >= 1:
		return resulting_data
	else:
		return "No existing data for this query"

