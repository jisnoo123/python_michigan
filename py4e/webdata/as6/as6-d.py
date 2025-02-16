import urllib.request
import json

url = input('Enter the url: ')

response = urllib.request.urlopen(url)
data = response.read().decode("utf-8")
json_data = json.loads(data)

# Process the JSON data
print(json_data)
info = json_data

s=0
for i in info['comments']:
    #print(i['count'])
    s=s+i['count']
print('sum=',s)