#Goal: Create a program that will read a given set of IPs, perform Geo IP and RDAP lookups, and accept a query to filter results.

import rdap
import geoip
import query_rdap
import query_geoip
import re



# opening File
class search():
	
	rdap_data = {}
	geoip_data = {}
	def __init__(self, ipIn):
		self.rdap_data[ipIn] = rdap.RDAP_search(ipIn)
		self.geoip_data[ipIn] = geoip.geoipSearch(ipIn) 
 

def RDAP_query():
	Options = ["Country", "Handle", "IP_Version", "Name", "Type", "Known_Phone_Numbers", "Known_Emails", "Known_Adresses"]

	print("Query Options: Country, Handle, IP_Version, Name, Type, Known_Phone_Numbers, Known_Emails, Known_Adresses" + '\n')
	while True:
		try:
			ui = raw_input("Number of Queries wanted (1-8): ")
   			val = int(ui)
   			break;
		except ValueError:
   			print("That's not an int!")

	if val < 9 and val > 0:
		opts = {}
		count = 0
		while count != val:
			"""option = raw_input("-| ")
			   option = option.split(" ")"""
			option = raw_input("Query type: ")
			print("\n")
			option_Input = raw_input("Input: ")
			#print(option)
			#print(Options)
			if option not in Options:
				print("Invalid option. Does not exist")
			elif option in opts:
				print("Invalid option. Already choosen.")
			else:
				opts[option] = option_Input
				count += 1
		query = query_rdap.query(opts, search.rdap_data)
		if type(query) is str:
			return query
		else:
			return "Query output: %s" %(query)


	else:
		print("Invalid input. Please try again")
		RDAP_query()

def GEO_query():
	# Filter options for Geo IP lookup
	Options = ["Country", "City", "CountryCode", "Timezone", "Region", "RegionName", "Zip_code"]
	print("Query Options: Country, City, CountryCode, Timezone, Region, RegionName, Zip_code" + '\n')
	
	while True:
		try:
			ui = raw_input("Number of Queries wanted (1-7): ")
   			val = int(ui)
   			break;
		except ValueError:
   			print("That's not an int!")



	if val < 8 and val > 0:
		opts = {}
		count = 0
		while count != val:
			print("Please copy and paste a Query type from the list above.")
			option = raw_input("Query type: ")
			print("\n")
			option_Input = raw_input("Input: ")
			
			if option not in Options:
				print("Invalid option. Does not exist")
			elif option in opts:
				print("Invalid option. Already choosen.")
			else:
				opts[option] = option_Input
				count += 1
		query = query_geoip.query(opts, search.geoip_data)
		if type(query) is str:
			return query
		else:
			return "Query output: %s" %(query)


	else:
		print("Invalid input. Please try again")
		GEO_query()



#file = raw_input("Enter file with IPs: ")
#myfile = open(file)
myfile = open('list_of_ips.txt')
print(myfile)
raw_text = str(myfile.readlines());
myfile.close();
#print(raw_text);

#parse through file using regular expression
ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', raw_text)

print("IPs Extracted: " + str(len(ips)))

if(raw_input("Would you like to print a list of parsed IPs? ")).upper() == "YES":
	print(ips)


# 20 - 50 IPs work best with the program

group = list(ips)

while True:
	try:
		ui = raw_input("Input Number of IPs to test: ")
		testing_number = int(ui)
   		break;
	except ValueError:
   			print("That's not a number!")


print("\nPlease wait while RDAP and GeoIP data loads.")

# Amount of IP used out of the parsed IPs
# Due to rate limits and loading time, I have kept testing under 50 IPs at a time

for ip in range(testing_number): 
	search(group[ip])

#RDAP Filter choice
while True:
	if(raw_input("Would you like to apply an RDAP Query Filter? ")).upper() == "YES":
		print RDAP_query()
	else:
		break

#GEO IP Filter choice
while True:
	if(raw_input("Would you like to apply a GEO_IP Query Filter? ")).upper() == "YES":
		print GEO_query()
	else:
		break


	





