from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
import json

random.seed(20161001)

def getLinks(articleUrl):
	html = urlopen("http://en.wikipedia.org" + articleUrl)
	bsObj = BeautifulSoup(html.read(), "html.parser")
	return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

def getHistoryIPs(pageUrl):
	pageUrl = pageUrl.replace("/wiki/", "")
	historyUrl = "http://en.wikipedia.org/w/index.php?title=" + pageUrl + "&action=history"
	print("History url is: " + historyUrl)
	html = urlopen(historyUrl)
	bsObj = BeautifulSoup(html.read(), "html.parser")
	ipAddresses = bsObj.findAll("a", {"class": "mw-userlink mw-anonuserlink"})
	addressList = set()
	for ipAddress in ipAddresses:
		addressList.add(ipAddress.get_text())
	return addressList

def getCountry(ipAddress):
	try:
		response = urlopen("http://freegeoip.net/json/" + ipAddress).read().decode("utf-8")
	except HTTPError:
		return None
	responseJson = json.loads(response)
	return responseJson.get("country_code")

links = getLinks("/wiki/Python_(programming_language)")

while(len(links) > 0):
	for link in links:
		print("------------------------------------------------")
		historyIPs = getHistoryIPs(link.attrs["href"])
		for historyIP in historyIPs:
			print(getCountry(historyIP))

	newLink = links[random.randint(0, len(links) - 1)].attrs["href"]
	links = getLinks(newLink)