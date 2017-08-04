import requests

url='https://api.ip2country.info/ip?12.45.6.15'

response=requests.get(url)
print(response)
print(response.content)

obj = response.json()
print(obj)

countryName=obj['countryName']
print(countryName)