import requests
from bs4 import BeautifulSoup
with open("sample.html",'r') as f:
    html_doc=f.read()
soup=BeautifulSoup(html_doc,'html.parser')

# to saw html content
# print(soup.prettify)

#how to title
print(soup.title,type(soup.title))

print(soup.title.name)

print(soup.title.string)

print(soup.title.parent.name)

print(soup.p)

# print(soup.p['class'])

print(soup.a)

print(soup.find_all('a'))


print(soup.find(id="link3"))

print(soup.find_all("div"))

print(soup.find_all("div")[1])

print(type(soup.find_all("div")))

for link in soup.find_all('a'):
    print(link.get('href'))