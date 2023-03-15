#For en bruker skal man kunne finne all informasjon om de kjøpene hen har gjort for fremtidige
#reiser. Denne funksjonaliteten skal programmeres.
import sqlite3

uuid=input("Legg inn uuid:")
con = sqlite3.connect("tog.db")
cursor = con.cursor()
cursor.execute(f"")
con.close()