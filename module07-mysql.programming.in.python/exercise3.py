import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root",
                               password="Secret_123", database="hrdb")

cur = conn.cursor()

cur.execute("""
    insert into employees values 
        (NULL,'jack bauer','tr1', 100000),
        (NULL,'kate austen','tr2', 200000),
        (NULL,'james sawyer','tr3', 300000),
        (NULL,'james sawyer','tr4', 400000)
""")

conn.commit()
print(f"last id: {cur.lastrowid}")
print(f"{cur.rowcount} record(s) inserted.")
