
# Initally planned on using free databases to query from, however, i failed to find reliable, free geo ip databases so I pivoted
# and decided to use web API

"""
using IP2LOCATION-LITE-DB11.CSV a free database for Geo IP Lookup

ip_from	INT (10) / DECIMAL (39,0)	First IP address in netblock.
ip_to	INT (10) / DECIMAL (39,0)	Last IP address in netblock.
country_code	CHAR(2)	Two-character country code based on ISO 3166.
country_name	VARCHAR(64)	Country name based on ISO 3166.
region_name	VARCHAR(128)	Region or state name.
city_name	VARCHAR(128)	City name.
latitude	DOUBLE	City latitude. Default to capital city latitude if city is unknown.
longitude	DOUBLE	City longitude. Default to capital city longitude if city is unknown.
zip_code	VARCHAR(30)	ZIP/Postal code.
time_zone	VARCHAR(8)	UTC time zone (with DST supported). 
If you are looking for Olson Time Zone, please visit here. 

import pandas as pd
import numpy as np


csv = pd.read_csv("IP2LOCATION-LITE-DB9.CSV", names = ["ip_from", "ip_to", "country_code", "country_name","region_name",
				  "city_name","latitude","longitude","zip_code"], low_memory = False)


csv_2 = pd.read_csv("GeoLite2-City-Blocks-IPv4.csv", names = [])
csv_3 = pd.read_csv("GeoLite2-City-Locations-en.csv", names = [])
print(csv.head())
print(csv.tail())"""



"""def determine ipZone(ip):
	ip = ip.replace(('.', ""))
	while ip >= csv["ip_from"].value:
		if(ip <= csv["ip_to"].value)

		print

"""

#      ["country", "city", "countryCode", "timezone", "region", "regionName", "zip", "lat", "lon"]


import json
import requests

def geoipSearch(ipIn):
	url = "http://ip-api.com/json/" + str(ipIn) + "?fields=country,countryCode,region,regionName,city,zip,timezone"
	try:
		web = requests.get(url)
		raw = web.content
		edit_string = raw.replace('"', "\"")
		data = json.loads(edit_string)
	except:
		data = {}
	try: #country
		Country = data["country"]
		Country.encode("ascii", "ignore")
	except:
		Country = "N/A" # No Data Avalible
	try: #City
		City = data["city"]
		City.encode("ascii", "ignore")
	except:
		City = "N/A" # No Data Avalible
	try: #CountryCode
		CountryCode = data["countryCode"]
		CountryCode.encode("ascii", "ignore")
	except:
		CountryCode = "N/A" # No Data Avalible
	try: #Timezone
		Timezone = data["timezone"]
		Timezone.encode("ascii", "ignore")
	except:
		Timezone = "N/A" # No Data Avalible
	try: #Region
		Region = data["region"]
		Region.encode("ascii", "ignore")
	except:
		Region = "N/A" # No Data Avalible
	try: #RegionName
		RegionName = data["regionName"]
		RegionName.encode("ascii", "ignore")
	except:
		RegionName = "N/A" # No Data Avalible
	try: #Zip_code
		Zip_code = data["zip"]
		Zip_code.encode("ascii", "ignore")
	except:
		Zip_code = "N/A" # No Data Avalible
	"""try: #country
					Latitude = str(data[lat])
					Latitude.encode("ascii", "ignore")
				except:
					Latitude = "N/A" # No Data Avalible
				try: #country
					Longitude = str(data[lon])
					Longitude.encode("ascii", "ignore")
				except:
					Longitude = "N/A" # No Data Avalible"""

	collected_data = [City, Country, CountryCode, Region, RegionName, Timezone, Zip_code]
	print("Geo_IP info: ")
	print(collected_data)
	return collected_data










