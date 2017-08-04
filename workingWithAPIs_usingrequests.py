import requests

url='http://api.open-notify.org/iss-now.json'

response=requests.get(url)

obj=response.json()
print(obj)
print(obj.get("iss_position").get("longitude"))