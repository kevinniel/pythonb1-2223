# utilisation de bs4
from bs4 import BeautifulSoup
# utilisation de requests
import requests

url = "https://books.toscrape.com/"

headers = {'Accept-Encoding': 'identity'}
r = requests.get(url, headers=headers)

print(r.text)