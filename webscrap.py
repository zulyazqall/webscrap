import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime

data = []
qoute = ['https://www.bloomberg.com/quote/SPX:IND', 'https://www.bloomberg.com/quote/CCMP:IND']

for pg in qoute:
    page = urllib2.urlopen(pg)

soup = BeautifulSoup(page, 'html.parser')
box = soup.find('h1',attrs={'class':'name'})
name = box.text.strip()
# print name

price_box = soup.find('div', attrs={'class':'price'})
price = price_box.text
# print price

data.append((name,price))
print data

with open('index.csv','a') as csv_file:
    writer = csv.writer(csv_file)
    for name, price in data:
        writer.writerow([name,price,datetime.now()])