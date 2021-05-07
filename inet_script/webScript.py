from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

# URLs (url_seller_brand_version_type)
url_inet_msi_3090_gamingXTrio = "https://www.inet.se/produkt/5411699/msi-geforce-rtx-3090-24gb-gaming-x-trio"

# Disguise requests as regular browser
req = Request(url_inet_msi_3090_gamingXTrio, headers={"User-Agent": "Mozilla/5.0"})

# Open url
uClient = urlopen(req)

# Save page
page_html = uClient.read()

# Close url
uClient.close()

# Parse html
page_soup = soup(page_html, "html.parser")

# Grabs box with price and availability
purchaseBox = page_soup.findAll("section",{"class":"box product-purchase"})

# Price
purchaseBox[0].div.div.span

# Stock
print(purchaseBox[0].button["aria-label"])