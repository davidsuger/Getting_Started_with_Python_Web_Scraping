import urllib.request
import re
from bs4 import BeautifulSoup
import csv

filename = "C:\Quan\Works\Projects\Python\WebPages\List of English monarchs - Wikipedia.htm"

with open(filename, encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html5lib')

for r in soup.select('.reference'):
    r.replace_with('')

table = []
n = 1
for t in soup.select(".wikitable tbody tr td b a")[:-1]:
    name = t.text
    # print(n, ' : ', [name])
    cell = t.find_parent('td')
    contents = cell.text.split('\n')

    try:
        date1 = contents[contents.index("–") - 1]
        date2 = contents[contents.index("–") + 1]
    except:
        date1 = contents[-3].replace('–', '')
        date2 = contents[-2].replace('–', '')

    print([name.strip(), date1.strip(), date2.strip()])
    n += 1
    table.append([name.strip(), date1.strip(), date2.strip()])

with open("monarchs.csv", 'w', encoding="utf-8", newline="")as f:
    writer = csv.writer(f)
    writer.writerows(table)
