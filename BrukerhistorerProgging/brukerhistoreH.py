#For en bruker skal man kunne finne all informasjon om de kjøpene hen har gjort for fremtidige
#reiser. Denne funksjonaliteten skal programmeres.

#Det blir for reiser etter der kjøpsdato er etter dagens dato
import sqlite3
from datetime import date


kundenummer=input("Legg inn kundenummer:")
con = sqlite3.connect("sql/tog.db")
cursor = con.cursor()

today = date.today()
cursor.execute(f" Select KundeOrdre.Ordrenummer, KundeOrdre.Dag, Billett.BillettID, Delstrekning.StartStasjon, Delstrekning.Endestasjon, TogruteForekomst.ForekomstID, TogruteForekomst.Ukedag \
               From KundeOrdre join Billett on (KundeOrdre.Ordrenummer = Billett.Ordrenummer) \
               join HarPlass on (Billett.BillettID = HarPlass.BillettID) \
               join TogruteForekomst on (Harplass.ForekomstID = TogruteForekomst.ForekomstID) \
               join Delstrekning on (Billett.DelstrekningID = Delstrekning.DelstrekningID) \
               Where KundeOrdre.Kundenummer == '{kundenummer}' AND KundeOrdre.Dag > {today};")
results = cursor.fetchall()

def FormatertSvar():
    s = ""
    for i in range(0,len(results)):
        s += (f"Ordrenummer: {results[i][0]} \nDag: {results[i][1]} \nUkedag: {results[i][6]} \nBilletID: {results[i][2]} \n{results[i][3]} til {results[i][4]} \nTogruteForekomst: {results[i][5]} \n\n")
    return s
print(FormatertSvar())
con.close()