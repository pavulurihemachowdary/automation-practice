import sqlite3

#establish a connection to database using sqlite3.connect()
con=sqlite3.connect('database.db')

#initialize the cursor
cur=con.cursor()

for i in cur.execute("select * from ips limit 5"):
    print(i)

#this returns the result as a list form
cur.execute("select address from ips limit 5")
print(cur.fetchall())