import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root",
                               password="Secret_123", database="hrdb")

cur = conn.cursor()

# cur.execute("create database hrdb")

cur.execute("""
    create table employees(
        id int(11) auto_increment primary key,
        full_name varchar(128) not null,
        iban varchar(128) not null,
        salary int(10)
    ) engine=innodb    
""")
