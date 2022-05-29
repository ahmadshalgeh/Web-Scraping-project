import requests
from bs4 import BeautifulSoup
import mysql.connector

mydb = mysql.connector.connect(user='root', password='my password',
                              host='127.0.0.1',
                              database="divar")

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE divar CHARACTER SET utf8 COLLATE utf8_general_ci;")
'''mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)'''

#mycursor.execute("CREATE TABLE cars(mizan_karkerd VARCHAR(255), gheymat VARCHAR(255))")

car = 'kia'
r  = requests.get('https://divar.ir/s/tehran/car?q=' + car)
soup = BeautifulSoup(r.text, 'html.parser')
val = soup.find_all('div',attrs={'class': 'kt-post-card__description'})
sql = "INSERT INTO cars (mizan_karkerd, gheymat) VALUES (%s, %s)"


for i in range(20):
    reshteh = val[i].text
    reshteh = reshteh.split('\n')
    #print(reshteh[0],reshteh[1])
    #print('-------------------------------------')
    s1 = reshteh[0]
    s2 = reshteh[1]
    val_sql = (s1, s2)
    mycursor.execute(sql, val_sql)

mydb.commit()



mycursor.close()