import requests

parameters = {"api_key":"moXqVS4GZoPjAtaJLNKgPTe4nYbk3EnqtnKQnbVb"}
# url = 'https://api.nasa.gov/planetary/earth/imagery'
url = 'https://api.nasa.gov/planetary/apod'

response = requests.get(url, params=parameters)

print(response)
print(response.content)

import pprint
pprint.pprint(response.json())