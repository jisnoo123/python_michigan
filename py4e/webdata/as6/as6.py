import requests
import json
def extract_json_data(url):
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the JSON data as a string
        json_data = response.text
        return json_data
    else:
        print(f"Error: Request failed with status code {response.status_code}")

# Example usage
url = input('Enter a url: ')
json_string = extract_json_data(url)
if json_string:
    # Process the JSON data string
    print(json_string)
info = json.loads(json_string)

s=0
for i in info['comments']:
    #print(i['count'])
    s=s+i['count']
print('sum=',s)