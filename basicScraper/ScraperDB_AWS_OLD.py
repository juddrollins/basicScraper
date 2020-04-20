import requests
from bs4 import BeautifulSoup
from csv import writer

#AWS SQL data base was deleted because of cost

import mysql.connector

mydb = mysql.connector.connect(
  host="database-2.crzbo2iybmfk.us-east-1.rds.amazonaws.com",
  port="3306",
  user="admin",
  database="mydatabase",
  passwd="password"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE drinks (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price INT)")


print(mydb)


# response = requests.get('https://shop.lowesfoods.com/shop/categories/3714')
#
# soup = BeautifulSoup(response.text, 'html.parser')
#
# posts = soup.find_all(class_='col')
#
# for post in posts:
#     print(post)
