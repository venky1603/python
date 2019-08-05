#Ex 12.04 - Following Links in Python
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Get the URL and get HTML parsed by BeautifulSoap
url = input('Enter - ')
count = input('Enter count - ')
position = input('Enter position - ')
for iteration in range(int(count)):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    tag = tags[int(position) - 1]
    url = tag.get('href', None)

print(tag.contents[0])
