import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import ssl
import requests
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



url = input('Enter url: ')

# Send a GET request to the URL
response = requests.get(url)

if response.status_code == 200:  # Successful request
    xm = response.text
stuff = ET.fromstring(xm)
lst = stuff.findall('comments/comment')
#print(xm)
s=0
for item in lst:
    #print('counts',item.find('count').text)
    s=s+int(item.find('count').text)
print('sum', s)