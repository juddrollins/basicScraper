import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://juddrollins.github.io/')

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='col')

for post in posts:
    print(post)
