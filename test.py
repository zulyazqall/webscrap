# import libraries
import urllib2
from bs4 import BeautifulSoup

# specify the url
qoute_page = "https://www.bloomberg.com/quote/SPX:IND"
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, ‘html.parser’)

# Take out the <div> of name and get its value
name_box = soup.find(‘td’, attrs={‘class’: ‘align-center’})

name = name_box.text.strip() # strip() is used to remove starting and trailing
print name

# get the index price
# price_box = soup.find(‘div’, attrs={‘class’:’price’})
# price = price_box.text
# print price