import urllib.request
import re
from bs4 import BeautifulSoup

url='https://en.wikipedia.org/wiki/List_of_English_monarchs'

response=urllib.request.urlopen(url)
html = response.read()

# print("html.parser: ", BeautifulSoup(html, "html.parser"))

# print("html5lib: ", BeautifulSoup(html, "html5lib"))

soup = BeautifulSoup(html, 'html5lib')
n=1
for t in soup.select(".wikitable tbody tr td b a"):
    print(n,' ++++++++++++++++++++++++++++++++++++++++++++=: ', t)
    print(t.find_parent('td').text)
    n+=1


# for t in soup.find_all("p"):
#     print('1: ', t)
# for t in soup.find_all(["th", "td"]):
#     print('2: ', t)
# for t in soup.find_all(class_="buzz"):
#     print('3: ', t)
# for t in soup.find_all(id=re.compile("^foo")):
#     print('4: ', t)
#
# for t in soup.select("p"):
#     print('1: ', t)
# for t in soup.select("th,td"):
#     print('2: ', t)
# for t in soup.select(".buzz"):
#     print('3: ', t)
# for t in soup.select("[id^=foo]"):
#     print('4: ', t)
#
# p = soup.select_one("[id^=foo]")
# print("p: ", p)
#
# print("parent: ",p.parent)
# print("next_sibling: ", p.find_next_sibling())
# print("next_sibling contents: ", p.find_next_sibling().content)
# print("previous_sibling: ", p.find_next_sibling().find_previous_sibling())
#
# p=soup.select_one("[name=fizz]")
# for t in p.children:
#     print("child: ",t)
#
# print(p.select_one("th"))
#
# print(p.attrs)
# p["id"]="bar"
# print(p.attrs)

