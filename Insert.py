import sqlite3
conn=sqlite3.connect("MitMorning1.db")
print("Tables created successfully")
conn.execute("INSERT INTO wanafunzii(ID,NAME,AGE,SCHOOL,GENDER)VALUES(1, 'ARIEL',30,'EMOBILIS','FEMALE') ")
conn.execute("INSERT INTO wanafunzii(ID,NAME,AGE,SCHOOL,GENDER)VALUES(2, 'VICTOR',18,'EMOBILIS','MALE') ")
conn.execute("INSERT INTO wanafunzii(ID,NAME,AGE,SCHOOL,GENDER)VALUES(3, 'MANVIN',30,'EMOBILIS','FEMALE') ")
conn.execute("INSERT INTO wanafunzii(ID,NAME,AGE,SCHOOL,GENDER)VALUES(4, 'NELIMA',30,'EMOBILIS','FEMALE') ")
conn.execute("INSERT INTO wanafunzii(ID,NAME,AGE,SCHOOL,GENDER)VALUES(5, 'CHROME',30,'EMOBILIS','FEMALE') ")
conn.execute("INSERT INTO wanafunzii(ID,NAME,AGE,SCHOOL,GENDER)VALUES(6, 'WINTER',30,'EMOBILIS','FEMALE') ")


conn.commit()
print("Records added successfully")
conn.close()