#Ex 12.03 Extracting data from web using Beautiful Soup
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
htmlPage = urlopen(url,context=ctx).read()
soup = BeautifulSoup(htmlPage, "html.parser")

#Retrieve all the <span> tags
tags = soup('span')
sum = 0
for tag in tags:
    content = tag.contents[0]
    sum = sum + int(content)

print(sum)
