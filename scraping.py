from bs4 import BeautifulSoup
import requests

# # HTML From File
# with open("index.html", "r") as f:
# 	doc = BeautifulSoup(f, "html.parser")

# tags = doc.find_all("p")[0]

# print(tags.find_all("b"))

# HTML From Website
url = "https://www.armcokenya.com/collections/bundled-offers/products/toshiba-55l3660-55-inch-digita-led-tv-full-hd"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")



prices = doc.find (
            'div', class_="detail-price").text.strip()
prices = prices[4:]  
prices=prices.replace(",","")

 

name = doc.find (
            'h1', class_="page-heading").text

sku = doc.find (
            'ul', class_="product-sku-collection").text.strip()
sku = sku[-6:]

availability = doc.find (
            'span', class_="stock").text



print(int(float(prices)))
print(name)
print(availability)
print(sku)

baseurl = "https://www.armcokenya.com"
# url=requests.get("https://www.armcokenya.com/collections/kitchen-appliances").text
# soup=BeautifulSoup(url,'html.parser')
# productlist = soup.find_all("div",{"class":"featured-img"})
# print(productlist)

# productlinks = []
# for x in range(1,4):
#   k = requests.get('https://www.armcokenya.com/collections/kitchen-appliances?pg={}&psize=24&sort=pasc'.format(x)).text  
#   soup=BeautifulSoup(k,'html.parser')  
#   productlist = soup.find_all("div",{"class":"featured-img"})


#   for product in productlist:
#         link = product.find("a",{"class":"boost-pfs-action-overlay"}).get('href')
#         productlinks.append(baseurl + link)
productlinks = []
for x in range(1,6):  
 k = requests.get('https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={}&psize=24&sort=pasc'.format(x)).text  
 soup=BeautifulSoup(k,'html.parser')  
 productlist = soup.find_all("li",{"class":"product-grid__item"})
 
 for product in productlist:
        link = product.find("a",{"class":"product-card"}).get('href')
        productlinks.append(baseurl + link)

print(productlinks)
