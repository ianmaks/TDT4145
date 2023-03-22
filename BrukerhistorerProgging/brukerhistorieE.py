#En bruker skal kunne registrere seg i kunderegisteret.
import sqlite3

def newUserID():
    con = sqlite3.connect("sql/tog.db")
    cursor = con.cursor()
    cursor.execute(f"SELECT MAX(Kundenummer) FROM Kunde;")
    results = cursor.fetchall()
    con.close()
    
    return 1 if results[0][0] == None else results[0][0]+1

navn=input("Legg inn navn: ")
epost=input("Legg inn epost: ")
mobilnummer=input("Legg inn mobilnummer: ")
kundenummer=newUserID();

con = sqlite3.connect("sql/tog.db")
cursor = con.cursor()
cursor.execute(f"INSERT INTO Kunde (Kundenummer, Navn, Epost, Mobilnummer) \
                VALUES ('{kundenummer}','{navn}' ,'{epost}' ,'{mobilnummer}');") 
con.commit()

print("Kunde registret! Ditt kundenummer er: ",kundenummer)
con.close()