import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter URL: ")

print("Retrieving " + url)
xfile = urllib.request.urlopen(url)
data = xfile.read()
print("Retrieved ", len(data), "characters")

info = json.loads(data)
ncount = len(info['comments'])
sum = 0

for item in info['comments']:
    sum = sum + int(item["count"])
    # print('Name:', item["name"])
    # print('Count:', item["count"])

print("Count:", ncount)
print("Sum:", sum)
