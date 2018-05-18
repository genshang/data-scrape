import urllib2
from bs4 import BeautifulSoup

web_page = "https://finance.yahoo.com/quote/FB?p=FB" #created a variable and assigned it the website from yahoo finance FB (getting the website)
page = urllib2.urlopen(web_page)# .urlopen is a function, web_page is the vessel for the website
# print(page)

soup = BeautifulSoup(page, "html.parser") #means we are going to parse through the html file. 

name_box = soup.find("h1", attrs={"class": "D(ib)"})
# print(name_box)
name = name_box.text
print(name)

price_box = soup.find("span", attrs={"class": "Fw(b)"})
price = price_box.text
print(price)

import csv #csv = comma separated value
from datetime import datetime

with open("index.csv", "w") as csv_file: #as is an alias, i.e. variable
    writer = csv.writer(csv_file)
    writer.writerow([name, price, datetime.now()])

