#For en bruker skal man kunne finne all informasjon om de kjøpene hen har gjort for fremtidige
#reiser. Denne funksjonaliteten skal programmeres.
import sqlite3

uuid=input("Legg inn kundenummer:")
con = sqlite3.connect("sql/tog.db")
cursor = con.cursor()
cursor.execute(f"")
results = cursor.fetchall()
print(results)
con.close()