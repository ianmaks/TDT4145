#Registrerte kunder skal kunne finne ledige billetter for en oppgitt strekning på en ønsket togrute 
#og kjøpe de billettene hen ønsker.
#
#Pass på at dere bare selger ledige plasser
import sqlite3
import itertools

togruter = ['dummy', 'Trondheim-Bodø-dagtog', 'Trondheim-Bodø-nattog', 'Mo i Rana-Trondheim-morgentog']

# SJEKKE ANTALL SETER I BRUK PÅ EN REISE
def check_avail(checks):
    con = sqlite3.connect("sql/tog.db")
    cursor = con.cursor()
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
    SELECT SUM(Plasser)
    FROM   Orders
    """)
    results = cursor.fetchall()
    con.close()
    if isinstance(results[0][0], int): 
        capacity.append((int) (results[0][0]))

# HENTE NY(TT) ORDRENUMMER/BILLETTID

def new_userID():
    con = sqlite3.connect("sql/tog.db")
    cursor = con.cursor()
    cursor.execute(f"SELECT MAX(BillettID) FROM Billett;")
    results = cursor.fetchall()
    con.close()
    return 1 if results[0][0] == None else results[0][0]+1

def hent_delstrekning():
    con = sqlite3.connect("sql/tog.db")
    cursor = con.cursor()
    cursor.execute(f"select DelstrekningID as targetDelstrekning from Delstrekning where Delstrekning.StartStasjon = '{start}' and Delstrekning.Endestasjon = '{slutt}';")
    results = cursor.fetchall()
    con.close()
    print(results)
    return results[0]

def hent_forekomstID():
    con = sqlite3.connect("sql/tog.db")
    cursor = con.cursor()
    cursor.execute(f"select ForekomstID from TogruteForekomst where TogruteID = '{togrute}' and Ukedag = '{ukedag}'")
    results = cursor.fetchall()
    con.close()
    print(results[0])
    return results[0][0]

def velg_vogn():
    if  togrute == 'Trondheim-Bodø-nattog':
        vogn = 'SJ-sovevogn-1'
    else:
        vogn = 'SJ-sittevogn-1'
    return vogn

# BESTILLE BILETTER

def fullfør_bestilling(antall_plasser):
    vogn = ""
    velg_vogn()
    con = sqlite3.connect("sql/tog.db")
    cursor = con.cursor()
    cursor.executescript(f"""
    insert into KundeOrdre (OrdreNummer, Dag, Tid, KundeNummer) values ('{new_userID}', date('now'), time('now'), '{kundenummer}');
    insert into Billett (BillettID, Ordrenummer, DelstrekningID, VognNavn) values ('{new_userID}', '{new_userID}', '{hent_delstrekning()}', '{vogn}');
    insert into HarPlass (BillettID, Plasser, ForekomstID) values ('{new_userID}', '{antall_plasser}', '{hent_forekomstID()}');
    """)

    con.commit()
    con.close()


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
    return checks



# KUNDESPØRRINGER
kundenummer=input("Legg inn kundenummer: ")
togrute = togruter[int(input("Velg togrute: \n (1) Trondheim-Bodø-dagtog \n (2) Trondheim-Bodø-nattog \n (3) Mo i Rana-Trondheim-morgentog \n Togrute: "))]
start=input("Startstasjon: ")
slutt=input("Sluttstasjon: ")
ukedag=input("Hvilken ukedag vil du reise på? ")

capacity = []
for i in set_checks(togrute):
    check_avail(i)
print(f"Det er {10 - max(capacity)} ledige plasser på denne reisen.")
if max(capacity) < 10:
    antall_plasser=input("Hvor mange plasser ønsker du å bestille? ")
    if (int) (antall_plasser) + max(capacity) <= 10:
        fullfør_bestilling(antall_plasser)    


