import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input("Enter URL: ")

print("Retrieving " + url)
xfile = urllib.request.urlopen(url).read()
print("Retrieved ", len(xfile), "characters")
tree = ET.fromstring(xfile)
results = tree.findall('comments/comment')
ncount = len(results)
sum = 0

for result in results:
    sum = sum + int(result.find('count').text)

print("Count: ", ncount)
print("Sum: ", sum)
