import urllib.request
import re
from bs4 import BeautifulSoup

html = '''
    <p id="foo1">f1</p>
    <p id="foo2">f2</p>
    <table name="fizz" class="buzz">
        <tr>
            <th>Letters</th>
            <th>Numbers</th>
        </tr>
        <tr>
            <td>A</td>
            <td>1</td>
        </tr>
        <tr>
            <td>B</td>
            <td>2</td>
        </tr>
        <tr>
            <td>C</td>
            <td>3</td>
        </tr>
    </table>
'''
print("html.parser: ", BeautifulSoup(html, "html.parser"))

print("html5lib: ", BeautifulSoup(html, "html5lib"))

soup = BeautifulSoup(html, 'html5lib')

for t in soup.find_all("p"):
    print('1: ', t)
for t in soup.find_all(["th", "td"]):
    print('2: ', t)
for t in soup.find_all(class_="buzz"):
    print('3: ', t)
for t in soup.find_all(id=re.compile("^foo")):
    print('4: ', t)

for t in soup.select("p"):
    print('1: ', t)
for t in soup.select("th,td"):
    print('2: ', t)
for t in soup.select(".buzz"):
    print('3: ', t)
for t in soup.select("[id^=foo]"):
    print('4: ', t)

p = soup.select_one("[id^=foo]")
print("p: ", p)

print("parent: ",p.parent)
print("next_sibling: ", p.find_next_sibling())
print("next_sibling contents: ", p.find_next_sibling().content)
print("previous_sibling: ", p.find_next_sibling().find_previous_sibling())

p=soup.select_one("[name=fizz]")
for t in p.children:
    print("child: ",t)

print(p.select_one("th"))

print(p.attrs)
p["id"]="bar"
print(p.attrs)

