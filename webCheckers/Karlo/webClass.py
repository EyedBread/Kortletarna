from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import sys
import json
import requests

class webhallen:

    url = "mall"
    name = "mall"

    def __init__(self,url,name):
        self.url = url
        self.name = name


    def func(self):
        result = requests.get(self.url)
        if result.status_code != 200:
            print("ERROR!")

        with requests.Session() as session:
            response = session.get(self.url).json()
            webStock = response["product"]["stock"]["web"]
            supplierStock = response["product"]["stock"]["supplier"]
            displayCap = response["product"]["stock"]["displayCap"] #Based on my findings this differintiates the products who are completely out of stock and the items that are out of stock in weblager but you can still order them(and maybe also available in certain retail shops)

        print("Product name:",self.name)
        if webStock == 0 and (supplierStock == 0 or supplierStock == None) and displayCap == 0:
            print("Slut i lager")
        else:
            if webStock == 0 and displayCap != 0:
                print("Slut i weblager. Beställningsvara")
            elif webStock != 0:
                print("I lager. Antal:",webStock)

class inet:

    url = "mall"
    name = "mall"

    def __init__(self,url,name):
        self.url = url
        self.name = name

    def func(self):
        req = Request(self.url,headers={"User-Agent": "Mozilla/5.0"})

        uClient = urlopen(req)

        page_html = uClient.read()

        uClient.close()

        page_soup = soup(page_html, "html.parser")

        purchaseBox = page_soup.findAll("section",{"class":"box product-purchase"}) #

        purchaseBox[0].div.div.span
        print('Product name:',self.name)
        if purchaseBox[0].button["aria-label"] == "Slutsåld": #
            print(purchaseBox[0].button["aria-label"])
        else:
            print("I lager")


#g1 = webhallen('https://www.webhallen.com/api/product/324223','ASUS GeForce RTX 3070 Dual OC 8GB')
g1.func()
g2 = webhallen('https://www.webhallen.com/api/product/324215','ASUS ROG STRIX GeForce RTX 3070 Gaming OC 8GB')
g2.func()
g3 = inet('https://www.inet.se/produkt/5411699/msi-geforce-rtx-3090-24gb-gaming-x-trio', 'MSI GeForce RTX 3090 24GB GAMING X TRIO')
g3.func()
g4 = inet('https://www.inet.se/produkt/6100527/logitech-g-pro-wireless', 'Logitech G PRO Wireless')
g4.func()