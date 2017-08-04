import urllib.request, json

url='http://api.open-notify.org/iss-now.json'

response=urllib.request.urlopen(url)
s = response.read()
print(s)

obj=json.loads(s.decode("utf8"))
print(obj)
print(obj.get("iss_position").get("longitude"))