import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root",
                               password="Secret_123", database="hrdb")

cur = conn.cursor()

cur.execute("""
    delete from employees where salary > 300000
""")

conn.commit()
print(f"{cur.rowcount} record(s) deleted.")
