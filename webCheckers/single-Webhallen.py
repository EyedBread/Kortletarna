from selenium import webdriver

print ("hello World!")
PATH = "./chromedriver.exe"
print ("hello World!")
driver = webdriver.Chrome(PATH)
print ("hello World!")
driver.get("https://www.webhallen.com/se/search?searchString=gtx&sort=searchRating&f=category%5E47&f=%2acategory%5E4684&f=attributes%5E110-1-NVIDIA%20GeForce%20RTX%203080~NVIDIA%20GeForce%20RTX%203060%20Ti~NVIDIA%20GeForce%20RTX%203070~NVIDIA%20GeForce%20RTX%203090~NVIDIA%20GeForce%20RTX%203060")