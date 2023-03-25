#Registrerte kunder skal kunne finne ledige billetter for en oppgitt strekning på en ønsket togrute 
#og kjøpe de billettene hen ønsker.
#
#Pass på at dere bare selger ledige plasser
import sqlite3
import itertools

togruter = ['Trondheim-Bodø-dagtog', 'Trondheim-Bodø-nattog', 'Mo i Rana-Trondheim-morgentog']

def check_avail(checks):
    cursor.execute(f"""
    
    WITH Orders
	AS (
    SELECT DISTINCT Billett.BillettID, Delstrekning.DelstrekningID, HarPlass.Plasser, TogruteForekomst.Ukedag
	FROM   Billett
    JOIN HarPlass on Billett.BillettID = HarPlass.BillettID
    JOIN TogruteForekomst on HarPlass.ForekomstID = TogruteForekomst.ForekomstID 
    JOIN TogRute on TogruteForekomst.TogruteID = TogRute.TogruteID 
    JOIN Delstrekning on Delstrekning.DelstrekningID = Billett.DelstrekningID 
    LEFT JOIN StrekningInnom on Delstrekning.DelstrekningID = StrekningInnom.DelstrekningID
    where (Delstrekning.StartStasjon = '{checks[0]}'
    OR Delstrekning.Endestasjon = '{checks[1]}'
    OR StrekningInnom.Stasjonsnavn =  '{checks[0]}'
    OR StrekningInnom.Stasjonsnavn = '{checks[1]}')
    AND TogRute.TogruteID = '{togrute}'
    AND TogruteForekomst.Ukedag = '{ukedag}'

    )
    SELECT *   
    FROM   Orders

    """)
    # BillettID, Ukedag, SUM(Plasser)

    
    results = cursor.fetchall()

    for i in results:
        print(checks[0], checks[1])
        print(i)
    print("")

con = sqlite3.connect("sql/tog.db")
cursor = con.cursor()

# VELG STASJONSREKKEFØLGE BASERT PÅ TOGRUTE
def set_checks(togrute):
    checks = []
    if togrute == 'Mo i Rana-Trondheim-morgentog':
        stasjoner = ['Mo i Rana', 'Mosjøen', 'Steinkjer', 'Trondheim']
        check_start = stasjoner.index(f"{start}")
        check_slutt = stasjoner.index(f"{slutt}")
        checks = list(itertools.combinations(stasjoner[check_start:check_slutt+1], 2))

    else:
        stasjoner = ["Trondheim", "Steinkjer", "Mosjøen", "Mo i Rana", "Fauske", "Bodø"]
        check_start = stasjoner.index(f"{start}")
        check_slutt = stasjoner.index(f"{slutt}")
        for i in range(check_start, check_slutt):
            checks.append((stasjoner[i], stasjoner[i+1]))
        print(checks)
    return checks

# KUNDESPØRRINGER
kundenummer=input("Legg inn kundenummer: ")
togrute = togruter[int(input("Velg togrute: \n (1) Trondheim-Bodø-dagtog \n (2) Trondheim-Bodø-nattog \n (3) Mo i Rana-Trondheim-morgentog \n Togrute: "))]
start=input("Startstasjon: ")
slutt=input("Sluttstasjon: ")
ukedag=input("Hvilken ukedag vil du reise på? ")


for i in set_checks(togrute):
    check_avail(i)

#kjope=input("angi hvilken du ønsker å kjøpe")

#cursor.execute(f"")


con.close()