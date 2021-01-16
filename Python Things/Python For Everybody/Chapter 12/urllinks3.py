from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

count = 0
sum = 0

# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
    numstr = tag.contents
    count = count + 1
    for n in numstr:
        no = int(n)
        sum = sum + no

print("Count " + str(count))
print("Sum " + str(sum))
