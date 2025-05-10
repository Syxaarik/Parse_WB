import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

art = 'https://www.wildberries.ru/catalog/0/search.aspx?search=12341234'
response = requests.get(art).text
soup = BeautifulSoup(response, 'lxml')

block = soup.find('div', class_='product-page__header')
text_name = soup.find('h', class_='product-page__title')

print(block)
