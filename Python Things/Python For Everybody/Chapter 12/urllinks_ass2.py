import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL: ')

count = int(input('Enter count: '))
position = int(input('Enter position: '))

# repeat to desired count
for i in range(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    ncount = 0
    for tag in tags:
        ncount = ncount + 1

        if ncount > position:
            break
        url = tag.get('href', None)
        print("Retrieving: " + url)
        name = tag.contents[0]

print(name)
