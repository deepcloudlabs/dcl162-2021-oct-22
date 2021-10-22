import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root",
                               password="Secret_123", database="world")

cur = conn.cursor()

cur.execute("""
    select ctry.name, city.name from country as ctry inner join city on ctry.capital = city.id
""")

for row in cur.fetchall():
    print(f"{row[0]:>16} => {row[1]:16}")
