import sqlite3

# conn = sqlite3.connect('test.db')

print("Opened datatbse succesffullyy ; ")

# conn.execute('''CREATE TABLE POSTS (
#          id INTEGER PRIMARY KEY AUTOINCREMENT,
#          username        TEXT    NOT NULL,
#          fullname        TEXT     NOT NULL,
#          userImg         TEXT     NOT NULL,
#          postImg         TEXT     NOT NULL);''')

# print("Table Created successfully")

sql = "INSERT INTO POSTS (username,fullname, userImg, postImg) VALUES('ahsan', 'John Keller', 'https://images.pexels.com/photos/614810/pexels-photo-614810.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500', 'https://images.pexels.com/photos/9730025/pexels-photo-9730025.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500')"

def insert(sql):
    conn = sqlite3.connect('test.db')
    conn.execute(sql)
    conn.commit()
    conn.close()
    return "success"


def execute_query(sql):
    conn = sqlite3.connect('test.db')
    cursor = conn.execute(sql)
    result = []
    for row in cursor:
        result.append(row)
    conn.commit()
    conn.close()
    return result


# sql = "SELECT * FROM POSTS"

print(insert(sql))

# conn.close()

