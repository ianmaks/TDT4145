#En bruker skal kunne registrere seg i kunderegisteret.
import sqlite3
from uuid import uuid4
navn=input("Legg inn navn: ")
epost=input("Legg inn epost: ")
mobilnummer=input("Legg inn mobilnummer: ")
kundenummer=uuid4()

con = sqlite3.connect("tog.db")
cursor = con.cursor()
cursor.execute(f"INSERT INTO Kunde \
                VALUES ({kundenummer},{navn} ,{epost} ,{mobilnummer});") 
#må vi her legge inn feil om den finnes? dumt med random kundenummer?
con.close()