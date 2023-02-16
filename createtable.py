import sqlite3
conn=sqlite3.connect("MitMorning1.db")
print("open database sucessfully")
conn.execute("CREATE TABLE wanafunzii(ID INT PRIMARY KEY NOT NULL,"
             "NAME TEXT NOT NULL,"
             "AGE INT NOT NULL,"
             "SCHOOL INT NOT NULL,"
             "GENDER TEXT NOT NULL)")
print("Tables created successfully")
conn.close()
