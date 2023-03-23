#Registrerte kunder skal kunne finne ledige billetter for en oppgitt strekning på en ønsket togrute 
#og kjøpe de billettene hen ønsker.
#
#Pass på at dere bare selger ledige plasser
import sqlite3

kundenummer=input("Legg inn kundenummer: ")
print("Velg togrute: \n (1) Trondheim-Bodø-dagtog \n (2) Trondheim-Bodø-nattog \n (3) Mo i Rana-Trondheim-morgentog")
togruter = ['Trondheim-Bodø-dagtog', 'Trondheim-Bodø-nattog', 'Mo i Rana-Trondheim-morgentog']
togrute = togruter[int(input("Togrute: "))]

start=input("Startstasjon: ")
slutt=input("Sluttstasjon: ")

con = sqlite3.connect("sql/tog.db")
cursor = con.cursor()

#cursor.execute(f"Insert into Billett (BillettID, Ordrenummer, DelstrekningID, VognNavn) values ()")
cursor.execute(f"SELECT Distinct Delstrekning.DelstrekningID, TogruteForekomst.ForekomstID, TogruteForekomst.Ukedag, Billett.BillettID from Billett join HarPlass on Billett.BillettID = HarPlass.BillettID join TogruteForekomst on HarPlass.ForekomstID = TogruteForekomst.ForekomstID join TogRute on TogruteForekomst.TogruteID = TogRute.TogruteID join Delstrekning on Delstrekning.DelstrekningID = Billett.DelstrekningID join RuteInnom on TogRute.TogruteID = RuteInnom.TogruteID where (Delstrekning.StartStasjon = '{start}' and Delstrekning.Endestasjon = '{slutt}') or (RuteInnom.Stasjonsnavn =  '{start}') or (RuteInnom.Stasjonsnavn =  '{slutt}')")





#kjope=input("angi hvilken du ønsker å kjøpe")

#cursor.execute(f"")

results = cursor.fetchall()
for i in results:
    print(i)
con.close()