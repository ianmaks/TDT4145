#En bruker skal kunne registrere seg i kunderegisteret.
import sqlite3
from uuid import uuid4
navn=input("Legg inn navn: ")
epost=input("Legg inn epost: ")
mobilnummer=input("Legg inn mobilnummer: ")
kundenummer=uuid4()

con = sqlite3.connect("python/TDT4145_prosjekt/sql/tog.db")
cursor = con.cursor()
cursor.execute(f"INSERT INTO Kunde \
                VALUES ({kundenummer},{navn} ,{epost} ,{mobilnummer});") 

print("Kunde registret! Ditt kundenummer er: ",kundenummer)
con.close()