import json
from urllib.request import urlopen

def getCountry(ipAddress):
	response = urlopen("http://freegeoip.net/json/" + ipAddress).read().decode("utf-8")
	responseJson = json.loads(response)
	return responseJson
	# return responseJson.get("country_code")

# print(getCountry("50.78.253.58"))
print(getCountry("99.245.99.252"))