import mysql.connector
"""
    1. Connection-oriented
    2. 1 TX per Connection -> Flat Model -> commit/rollback
    3. isolation level: READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE
"""
conn = mysql.connector.connect(host="localhost", user="root",
                               password="Secret_123", database="hrdb")

cur = conn.cursor()

cur.execute("""
    set session transaction isolation level READ UNCOMMITTED
""")

cur.execute("""
    update employees set salary = salary * 2
""")

conn.commit()
print(f"{cur.rowcount} record(s) updated.")
