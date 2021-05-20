from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import sys
import json
import requests
from notifications import notification_slack
from config import *
from gui import *
from urllib.error import HTTPError, URLError

#
def webhallenFunc(url,name):
    result = requests.get(url)
    if result.status_code != 200:
        print("ERROR!")
        return

    with requests.Session() as session:
        response = session.get(url).json()
        webStock = response["product"]["stock"]["web"]
        supplierStock = response["product"]["stock"]["supplier"]
        displayCap = response["product"]["stock"]["displayCap"] #Based on my findings this differintiates the products who are completely out of stock and the items that are out of stock in weblager but you can still order them(and maybe also available in certain retail shops)

    print("Product name:",name)
    if webStock == 0 and (supplierStock == 0 or supplierStock == None) and displayCap == 0:
        print("Slut i lager")
    else:
        if webStock == 0 and displayCap != 0:
            print("Slut i weblager. Beställningsvara")
        elif webStock != 0:
            print("I lager")
            if MSG_POPUP_GUI: stockTrue(url,name,"webhallen")
            if MSG_SEND_SLACK: notification_slack(url,webStock)


def inetFunc(url,name):
    page_soup = parseHTML(url)
    if page_soup == "exit":
        return
    else:
        purchaseBox = page_soup.findAll("section",{"class":"box product-purchase"}) #
        print('Product name:',name)
        #print(purchaseBox[0].button["class"])
        if "disabled" not in purchaseBox[0].button["class"]:
            print("I lager")
            if MSG_POPUP_GUI: stockTrue(url,name,"inet")
            if MSG_SEND_SLACK: notification_slack(url,1)
        else:
            print("Slut i lager")

def proshopFunc(url,name):
    page_soup = parseHTML(url)
    if page_soup == "exit":
        return
    else:
        purchaseBox = page_soup.find("div",{"class":"site-stock-text site-inline"})
        print("Product name:",name)
        if "I lager" not in purchaseBox.get_text():
            print("Slut i lager")
        elif "I lager" in purchaseBox.get_text():
            print("I lager")
            if MSG_POPUP_GUI: stockTrue(url,name,"proshop")
            if MSG_SEND_SLACK: notification_slack(url, 1)
        else:
            print("Error?")

def parseHTML(url):
    try:
        req = Request(url,headers={"User-Agent": "Mozilla/5.0"})

        uClient = urlopen(req)

        page_html = uClient.read()

        uClient.close()

        page_soup = soup(page_html, "html.parser")

        return page_soup

    except HTTPError as error:
        print('Error in loading page')
        return "exit"
    except URLError as error:
        print('Error in URL')
        return "exit"

#webhallenFunc('https://www.webhallen.com/api/product/324223','ASUS GeForce RTX 3070 Dual OC 8GB') #Ej i lager
#webhallenFunc('https://www.webhallen.com/api/product/324215','ASUS ROG STRIX GeForce RTX 3070 Gaming OC 8GB') #Ej i lager

#inetFunc('https://www.inet.se/produkt/5411699/msi-geforce-rtx-3090-24gb-gaming-x-trio', 'MSI GeForce RTX 3090 24GB GAMING X TRIO') #Ej i lager
#inetFunc('https://www.inet.se/produkt/6100527/logitech-g-pro-wireless', 'Logitech G PRO Wireless') #I lagera

#proshopFunc('https://www.proshop.se/Grafikkort/MSI-GeForce-RTX-3070-VENTUS-2X-OC-8GB-GDDR6-SDRAM-Grafikkort/2876873', 'MSI GeForce RTX 3070 VENTUS 2X OC - 8GB GDDR6 SDRAM') # ej i lager
#proshopFunc('https://www.proshop.se/Chassi-tillbehoer/DUTZO-Anti-sag-bracket-for-graphics-cards-ARGB/2861535', 'nånting') # är i lager
