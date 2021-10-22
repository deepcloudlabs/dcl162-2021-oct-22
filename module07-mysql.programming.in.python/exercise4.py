import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root",
                               password="Secret_123", database="hrdb")

cur = conn.cursor()

cur.execute("""
    select full_name,salary,iban from employees limit 2,3
""")

for row in cur.fetchall():
    # print(type(row).__name__)
    print(f"{row[0]:>16}: {row[1]:6} --> {row[2]:>10}")
