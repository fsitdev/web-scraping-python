# import the library used to query a website
import urllib2
import xlwt
result = xlwt.Workbook()
sheet = result.add_sheet("product info")
sheet.write(0, 1, "Product Name")
sheet.write(0, 2, "Price")
# specify the url
wiki = "https://www.frankana.de/de/sale/monatsangebot.html"
# import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
page = urllib2.urlopen(wiki)
# Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page, "html.parser")
all_products = soup.find_all("li", {"class": "item last"})
index = 0
for product in all_products:
    productname = product.find("h2", {"class": "product-name"}).find("a").get("title")
    index = index + 1
    sheet.write(index, 1, productname)
    price = product.find("div", {"class": "price-box"}).find_all("span", {"class": "price"})[-1].text
    sheet.write(index, 2, price)
result.save("product list.xls")