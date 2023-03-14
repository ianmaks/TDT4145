import sqlite3
con = sqlite3.connect("tog.db")
cursor = con.cursor()
cursor.execute("SELECT * FROM tog")
con.close()
