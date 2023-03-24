#Registrerte kunder skal kunne finne ledige billetter for en oppgitt strekning på en ønsket togrute 
#og kjøpe de billettene hen ønsker.
#
#Pass på at dere bare selger ledige plasser
import sqlite3
import itertools


def check_avail(checks):
    cursor.execute(f"""
    
    WITH Orders
	AS (SELECT DISTINCT Delstrekning.DelstrekningID, HarPlass.Plasser
	FROM   Billett
    JOIN HarPlass on Billett.BillettID = HarPlass.BillettID
    JOIN TogruteForekomst on HarPlass.ForekomstID = TogruteForekomst.ForekomstID 
    JOIN TogRute on TogruteForekomst.TogruteID = TogRute.TogruteID 
    JOIN Delstrekning on Delstrekning.DelstrekningID = Billett.DelstrekningID 
    LEFT JOIN StrekningInnom on Delstrekning.DelstrekningID = StrekningInnom.DelstrekningID
    where (Delstrekning.StartStasjon = '{checks[0]}')
    OR (Delstrekning.Endestasjon = '{checks[1]}') 
    OR (StrekningInnom.Stasjonsnavn =  '{checks[0]}') 
    OR (StrekningInnom.Stasjonsnavn = '{checks[1]}'))
    SELECT DelstrekningID, Plasser, SUM(Plasser)       
    FROM   Orders

    """)
    
    results = cursor.fetchall()

    for i in results:
        print(checks[0], checks[1])
        print(i)
    print("")

con = sqlite3.connect("sql/tog.db")
cursor = con.cursor()

kundenummer=input("Legg inn kundenummer: ")
print("Velg togrute: \n (1) Trondheim-Bodø-dagtog \n (2) Trondheim-Bodø-nattog \n (3) Mo i Rana-Trondheim-morgentog")
togruter = ['Trondheim-Bodø-dagtog', 'Trondheim-Bodø-nattog', 'Mo i Rana-Trondheim-morgentog']
togrute = togruter[int(input("Togrute: "))]

start=input("Startstasjon: ")
slutt=input("Sluttstasjon: ")



#cursor.execute(f"Insert into Billett (BillettID, Ordrenummer, DelstrekningID, VognNavn) values ()")

if togrute == 'Mo i Rana-Trondheim-morgentog':
    stasjoner = ['Mo i Rana', 'Mosjøen', 'Steinkjer', 'Trondheim']
    check_start = stasjoner.index(f"{start}")
    check_slutt = stasjoner.index(f"{slutt}")
    checks = list(itertools.combinations(stasjoner[check_start:check_slutt+1], 2))

else:
    stasjoner = ["Trondheim", "Steinkjer", "Mosjøen", "Mo i Rana", "Fauske", "Bodø"]
    check_start = stasjoner.index(f"{start}")
    check_slutt = stasjoner.index(f"{slutt}")
    checks = list(itertools.combinations(stasjoner[check_start:check_slutt+1], 2))

for i in checks:
    check_avail(i)





#cursor.execute(f"SELECT distinct TogRute.Startstasjon,TogRute.Endestasjon, RI1.Stasjonsnavn, RI2.Stasjonsnavn  from TogruteForekomst join TogRute on TogruteForekomst.TogruteID = TogRute.TogruteID join RuteInnom as RI1 on TogruteForekomst.TogruteID = RI1.TogruteID join RuteInnom as RI2 on TogruteForekomst.TogruteID = RI2.TogruteID join Delstrekning where (Delstrekning.StartStasjon = RI1.Stasjonsnavn and Delstrekning.Endestasjon = RI2.Stasjonsnavn)")
#               (Delstrekning.StartStasjon = TogRute.Startstasjon and Delstrekning.Endestasjon = RuteInnom.Stasjonsnavn) or (Delstrekning.StartStasjon = RuteInnom.Stasjonsnavn and Delstrekning.Endestasjon = TogRute.Endestasjon) or (Delstrekning.StartStasjon = RuteInnom.Stasjonsnavn and Delstrekning.Endestasjon = RuteInnom.Stasjonsnavn)")
#Delstrekning.DelstrekningID,  TogruteForekomst.ForekomstID, TogruteForekomst.Ukedag
#on 
# results = cursor.fetchall()

# for i in results:
#     print(i)



#kjope=input("angi hvilken du ønsker å kjøpe")

#cursor.execute(f"")


con.close()