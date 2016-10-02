import requests as rq

params = {"firstname": "Zhe", "lastname": "Wang"}
r = rq.post("http://pythonscraping.com/files/processing.php", data=params)
print(r.text)