

Challange: Create a program that will read a given set of IPs, perform Geo IP and RDAP lookups, and accept a query to filter results.



Objectives of this challange:
	-	Take abstract requirements and run with them
	-	Write isolated decoupled modules with strict input/output interfaces
	-	Create a query language and algorithm for filtering
	-	Reading, parsing, and extracting IP addresses from unstructured text in an efficient manner



IP Parsing:
	I utilized regular expression to parse thorugh the given document for the 5000 Ips and store them in a list. This takes place in iparse.py (the driver file).



RDAP lookups and filtering:
	Using Web API, (http://rdap.apnic.net/ip/ + ip), my program retrevies 8 data points on each IP address in the testing group (Country, Handle, IP_Version, Name, Type, Known_Phone_Numbers, Known_Emails, Known_Adresses). This takes quite a bit of time to load, especially for larger testing groups, however it results in quick data access afterwards. Using a database rather than Web API would make the program independent and faster, however my search for a reliable and free RDAP look up database was not sucessful. This data retrival takes place in rdap.py. Additionally, the API was relativley incosistent, failing to find data for many IPs in various catagories. 

	The RDAP filtering of the IPs takes place in query_rdap.py. Querying depends on  user input and is preformed by comparing key value pairs 
	(key = query option and value = user input) to the data store {rdap_data}. The query languge is relativley weak and requires precision in the input.
	
	A few examples are provide below for assistence. 		

	Example:																																		An exapmple of a specific IP adress data block:
		
		[Country, Handle,	IP_Version, Name, Type,  Known_Phone_Numbers,  Known_Emails, Known_Adresses]
		["ES", "81.44.0.0 - 81.44.255.255",  "v4", "RIMA", "ASSIGNED PA", "N/A", ["nemesys@telefonica.es"], ["C/ Ronda de la Comunicaci?n s/n"]]

		Query type: IP_Version
		Input: v4

		Query type: Country
		input: ES



GEO_IP lookups and filtering:
	At first, I attempted to find sutible, free databases for Geo IP lookups to query from. The databases I found were not very consistent so I decided to pivot and use Web API. This website was the most reliable and free, however has a 150 query per minute rate limit. The API retrives 7 data points for each IP in the testing group [Country, City, CountryCode, Timezone, Region, RegionName, Zip_code]. This API seems more consistent than the RDAP API used, however, still fails to find data for specific fields.

	Filtering of the GEO IP lookups takes place in query_geoip.py. Querying depends on  user input and is preformed by comparing key value pairs (key = query option and value = user input) to the data store {geoip_data}. The query languge is relativley weak and requires precision in the input.

	Examples:

		GEO IP Filter Input Example:

		[ "Country", "		    	City", 		"CountryCode",   	"Timezone", 		"Region", 	"RegionName",	 "Zip_code"]
		['United States', 		  'Columbus',		'US', 	    'America/New_York', 	  'OH', 	   'Ohio',	       '43218']

		Query type: Country
		Input: United States

		Query type: Zip_code
		Input: 43218


Running the Program:
	Program runs simply through terminal. I used Python 2.7.10 and packages including re, json, requests to preform needed functions. User input needs to be precise, examples above for reference.

Reflection:
	This was a challanging and very intriguing project for me. With more time, I would have figured out an alternative to the rate limitations for the RDAP and GEO IP look up sites. 







