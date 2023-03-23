#Registrerte kunder skal kunne finne ledige billetter for en oppgitt strekning på en ønsket togrute 
#og kjøpe de billettene hen ønsker.
#
#Pass på at dere bare selger ledige plasser
import sqlite3

kundenummer=input("Legg inn kundenummer: ")
print("Velg togrute: \n (1) Trondheim-Bodø-dagtog \n (2) Trondheim-Bodø-nattog \n (3) Mo i Rana-Trondheim-morgentog")
togruter = ['Trondheim-Bodø-dagtog', 'Trondheim-Bodø-nattog', 'Mo i Rana-Trondheim-morgentog']
togrute = togruter[int(input())]

start=input("Startstasjon: ")
slutt=input("Sluttstasjon: ")

con = sqlite3.connect("sql/tog.db")
cursor = con.cursor()

#cursor.execute(f"select TogRute.TogruteID as Rutenavn, TogruteForekomst.Ukedag as Dag from TogRute join TogruteForekomst where TogRute.TogruteID = TogruteForekomst.TogruteID")

#cursor.execute(f"select Delstrekning.DelstrekningID as ID, Delstrekning.StartStasjon as Start, Delstrekning.Endestasjon as Ende, BestårAv.BaneStrekningNavn as BaneNavn from BestårAv join Delstrekning where BestårAv.DelstrekningID = Delstrekning.DelstrekningID and Delstrekning.StartStasjon = '{start}' and Delstrekning.Endestasjon = '{slutt}'")

cursor.execute(f"select TogruteForekomst.ForekomstID from Delstrekning join BestårAv join Banestrekning join TogRute join TogruteForekomst")

#kjope=input("angi hvilken du ønsker å kjøpe")

#cursor.execute(f"")

results = cursor.fetchall()
for i in results:
    print(i)
con.close()