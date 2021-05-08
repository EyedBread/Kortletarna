import sys
import time
import json
import requests
import urllib.request
from bs4 import BeautifulSoup as bs
from random import randrange


# Setup

# Api URLs
URL = [
       #3090
       "https://www.webhallen.com/api/product/331727-Zotac-Gaming-GeForce-RTX-3090-Trinity-24GB-OC",
       "https://www.webhallen.com/api/product/324101-ASUS-ROG-STRIX-GeForce-RTX-3090-24GB-Gaming-OC",
       "https://www.webhallen.com/api/product/324063-ASUS-TUF-GeForce-RTX-3090-24GB-Gaming-OC",
       "https://www.webhallen.com/api/product/324070-MSI-GeForce-RTX-3090-GAMING-X-TRIO-24GB",
       "https://www.webhallen.com/api/product/329090-ASUS-ROG-STRIX-GeForce-RTX-3090-Gaming-OC-24GB-GDDR6X-Vit",
       "https://www.webhallen.com/api/product/328719-Gigabyte-GeForce-RTX-3090-Turbo-24GB"
       #3080

       #3070

       #3060
]

# Real URLs
Real_URL = [
       #3090
       "https://www.webhallen.com/se/product/331727-Zotac-Gaming-GeForce-RTX-3090-Trinity-24GB-OC",
       "https://www.webhallen.com/se/product/324101-ASUS-ROG-STRIX-GeForce-RTX-3090-24GB-Gaming-OC",
       "https://www.webhallen.com/se/product/324063-ASUS-TUF-GeForce-RTX-3090-24GB-Gaming-OC",
       "https://www.webhallen.com/se/product/324070-MSI-GeForce-RTX-3090-GAMING-X-TRIO-24GB",
       "https://www.webhallen.com/se/product/329090-ASUS-ROG-STRIX-GeForce-RTX-3090-Gaming-OC-24GB-GDDR6X-Vit",
       "https://www.webhallen.com/se/product/328719-Gigabyte-GeForce-RTX-3090-Turbo-24GB"
       #3080

       #3070

       #3060

]

# Settings (OBS!! Insert personal webhook)
running = True
found = False
refreshTime = 37# seconds
webhook_url = "insert_webhook_url_here"



while running:

    card_nb = randrange(len(URL))
    

    result = requests.get(URL[card_nb])
    if result.status_code != 200:
        print("ERROR!")

    #print(result.headers)

    print("\n")

    with requests.Session() as session:
        response = session.get(URL[card_nb]).json()
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
            print(URL[card_nb])
            found = True
    
    if found:
        found = False
        message = "In stock: " + Real_URL[card_nb]
        slack_data = {'text': message}
        data = json.dumps(slack_data)
        response = requests.post(
            webhook_url, data,
            headers={'Content-Type': 'application/json'}
        )
        if response.status_code != 200:
            raise ValueError(
                'Request to slack returned an error %s, the response is:\n%s'
                % (response.status_code, response.text)
        )
        
        
    time.sleep(refreshTime)
    
