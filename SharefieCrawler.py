import requests
from bs4 import BeautifulSoup


resp = requests.get('https://www.sharefie.net/post/7206')
# print(resp)

soup = BeautifulSoup(resp.text, 'html.parser')
# print(soup)

selector = soup.select("img")
# print(selector)

for select in selector:
    print(select["data-src"])

