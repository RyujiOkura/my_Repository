from bs4 import BeautifulSoup
import re

with open('typhoon.html') as f:
    soup = BeautifulSoup(f, 'html.parser')

year = []
num = []

for td in soup.find_all('td', align="center"):
    r = re.search(r'(20|19)[^<]+$', td.text)
    if (r != None):
        year.append(r.group(0))
    else:
        num.append(td.text)

for i in range(len(year)):
    print(year[i] + " : " + num[i])

