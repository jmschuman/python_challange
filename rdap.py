import re
import json
import requests


# [Country, Handle, IP_Version, Name, Type, Known_Phone_Numbers, Known_Emails, Known_Adresses]

def RDAP_search(ipIn):
	#url for RDAP look up
	url = 'http://rdap.apnic.net/ip/' + str(ipIn) #ip adress on the end
	#series of try except blocks to handle errors
	try:
		web = requests.get(url)
		raw = web.content
		edit_string = raw.replace('"', "\"")
		data = json.loads(edit_string)
	except:
		data = {} #Error handling

	try: #country
		Country = data["country"]
		Country.encode("ascii", "ignore")
	except:
		Country = "N/A" # No Data Avalible
	try: #Handle
		Handle = data["handle"]
		Handle.encode("ascii", "ignore")
	except:
		Handle = "N/A" # No Data Avalible
	try: #IP_Version
		IP_Version = data["ipVersion"]
		IP_Version.encode("ascii", "ignore")
	except:
		IP_Version = "N/A" # No Data Avalible
	try: #Node Name
		Name = data["name"]
		Name.encode("ascii", "ignore")
	except:
		Name = "N/A" # No Data Avalible
	try: # Type
		Type = data["type"]
		Type.encode("ascii", "ignore")
	except:
		Type = "N/A" # No Data Avalible
	
	temp = str(data)
	try: # Known_Phone_Numbers
		nums = re.findall(u"'text', (.*?)]", temp)
		Known_Phone_Numbers = []
		for n in nums:
			if '+' in n and "-" in n:
				digit = i[2:-1]
				Known_Phone_Numbers.append(digit)
		Known_Phone_Numbers = list(set(number))
	except:
		Known_Phone_Numbers = "N/A" # No Data Avalible
	try: #Known_Emails
		emails = re.findall(u"'email', (.*?)]", temp)
		Known_Emails = []
		for e in emails:
			email = e.split(" ")
			Known_Emails.append(email[-1][2:-1])
		Known_Emails = list(set(Known_Emails))
	except:
		Known_Emails = "N/A" # No Data Avalible
	try: #Known_Adresses
		adresses = re.findall(u"'label':(.*?)}", temp)
		Known_Adresses = []
		for a in adresses:
			temp = a.replace("\\n", " ")
			Known_Adresses.append(temp[3:-1])
		Known_Adresses = list(set(Known_Adresses))
	except:
		Known_Adresses = "N/A" # No Data Avalible



	# array of all colelcted data to be returned
	collected_data = [Country, Handle, IP_Version, Name, Type, Known_Phone_Numbers, Known_Emails, Known_Adresses]
	#print(collected_data)
	print("RDAP info: ")
	print collected_data
	return collected_data
	

	
