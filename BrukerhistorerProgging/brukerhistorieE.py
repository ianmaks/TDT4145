#En bruker skal kunne registrere seg i kunderegisteret.
import sqlite3
from uuid import uuid4
navn=input("Legg inn navn: ")
epost=input("Legg inn epost: ")
mobilnummer=input("Legg inn mobilnummer: ")
kundenummer=uuid4()

con = sqlite3.connect("sql/tog.db")
cursor = con.cursor()
cursor.execute(f"INSERT INTO Kunde (Kundenummer, Navn, Epost, Mobilnummer) \
                VALUES ('{kundenummer}','{navn}' ,'{epost}' ,'{mobilnummer}');") 
con.commit()

print("Kunde registret! Ditt kundenummer er: ",kundenummer)
con.close()