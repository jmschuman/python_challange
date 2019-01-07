
""" RDAP QUERY FUNCTION """

def query(opts, data):
	# lists
	listOptions = ["Known_Phone_Numbers", "Known_Emails", "Known_Adresses"]
	# nonList queries
	simpleOptions = ["Country", "Handle", "IP_Version", "Name", "Type"]

	resulting_data = []

	for a,b in data.items():
		c = 0
		for o in opts:
			if o in simpleOptions:
				if str(b[simpleOptions.index(o)]) == str(opts[o]):
					c += 1
			if o in listOptions:
				if str(opts[o]) in b[listOptions.index(o) + 5]:
					c += 1
		if c == len(list(opts)):
			resulting_data.append(a)

	
	if len(resulting_data) >= 1:
		return resulting_data
	else:
		return "No existing data for this query"





