from urllib.request import urlopen
from bs4 import BeautifulSoup

import datetime
import random
import re

# random.seed(datetime.datetime.now())
random.seed(20161001)
def getLinks(articleUrl):
	html = urlopen("http://en.wikipedia.org{}".format(articleUrl))
	bsObj = BeautifulSoup(html.read(), "html.parser")
	return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/python")
while len(links) > 0:
	newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
	print(newArticle)
	input()
	links = getLinks(newArticle)


# from urllib.request import urlretrieve
# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# import re
# import json

# html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
# bsObj = BeautifulSoup(html.read(), "html.parser")

# for link in bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
# 	if "href" in link.attrs:
# 		print(link.attrs["href"])
# for link in bsObj.findAll("a"):
# 	if "href" in link.attrs:
# 		print(link.attrs["href"])

# print(bsObj)
# print(bsObj.h1)

# for i in dir(bsObj)clc:
# 	print("This is : ", i)

# print(dir(bsObj))
# imageLocation = bsObj.find("a", {"id": "logo"}).find("img")["src"]
# urlretrieve(imageLocation, "./image/logo.jpg")