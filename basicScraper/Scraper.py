import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://www.youtube.com/')

soup = BeautifulSoup(response.text, 'html.parser')

