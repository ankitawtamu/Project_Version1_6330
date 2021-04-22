import sqlite3


con = sqlite3.connect('./flaskr/db.sqlite')
cur = con.cursor()


x = cur.execute("delete from Store where id = 1")

#x = cur.execute("select * from Store")
#cur.execute("select * from Store where id = 1")

print(x.fetchone())

con.close()

#good
#run this