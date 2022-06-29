import sqlite3

conn = sqlite3.connect('test.db')

print("Opened datatbse succesffullyy ; ")

# conn.execute('''CREATE TABLE USER
#          (ID INT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          SOCKETID       TEXT     NOT NULL);''')

# print("Table Created successfully")

def insert(sql):
    conn.execute(sql)
    print("Inserted successfully")

conn.close()