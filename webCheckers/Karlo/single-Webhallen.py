import sys
import json
import requests
import urllib.request
from bs4 import BeautifulSoup as bs


URL = "https://www.webhallen.com/api/product/324215" #ASUS TUF GeForce RTX 3070 8GB Gaming OC
#URL = "https://www.webhallen.com/api/product/322879" #elscooter är i weblager
#URL = "https://www.webhallen.com/api/product/315277" #Asus TUF VG27AQ fyndvara är ej i weblager men är en beställningsvara och kan 


result = requests.get(URL)
if result.status_code != 200:
    print("ERROR!")

#print(result.headers)

print("\n")

with requests.Session() as session:
    response = session.get(URL).json()
    webStock = response["product"]["stock"]["web"]
    supplierStock = response["product"]["stock"]["supplier"]
    displayCap = response["product"]["stock"]["displayCap"] #Based on my findings this differintiates the products who are completely out of stock and the items that are out of stock in weblager but you can still order them(and maybe also available in certain retail shops)
    name = response["product"]["name"]

print("Product name:",name)
if webStock == 0 and (supplierStock == 0 or supplierStock == None) and displayCap == 0:
    print("Out of stock")
else:
    if webStock == 0 and displayCap != 0:
        print("Out of stock in weblager. Beställningsvara")
    elif webStock != 0:
        print("In stock. Current available amount:",webStock)