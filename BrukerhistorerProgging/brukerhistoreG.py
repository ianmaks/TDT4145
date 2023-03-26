#Registrerte kunder skal kunne finne ledige billetter for en oppgitt strekning på en ønsket togrute 
#og kjøpe de billettene hen ønsker.
#
#Pass på at dere bare selger ledige plasser
import datetime
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
    JOIN KundeOrdre on KundeOrdre.OrdreNummer = Billett.Ordrenummer
    JOIN HarPlass on Billett.BillettID = HarPlass.BillettID
    JOIN TogruteForekomst on HarPlass.ForekomstID = TogruteForekomst.ForekomstID 
    JOIN TogRute on TogruteForekomst.TogruteID = TogRute.TogruteID 
    JOIN Delstrekning on Delstrekning.DelstrekningID = Billett.DelstrekningID
    JOIN Oppsett on Oppsett.TogruteID = TogRute.TogruteID
    JOIN VognType on Oppsett.VognNavn = VognType.VognNavn
    LEFT JOIN StrekningInnom on Delstrekning.DelstrekningID = StrekningInnom.DelstrekningID
    where (Delstrekning.StartStasjon = :checksnull
    OR Delstrekning.Endestasjon = :checksone
    OR StrekningInnom.Stasjonsnavn =  :checksnull
    OR StrekningInnom.Stasjonsnavn = :checksone)
    AND TogRute.TogruteID = :togrute
    AND TogruteForekomst.Ukedag = :ukedag
    )
    SELECT SUM(Plasser)
    FROM   Orders;
    """,
    {"checksnull": checks[0],
     "checksone": checks[1],
     "togrute": togrute,
     "ukedag": ukedag
     })
    results = cursor.fetchall()
    con.close()
    if isinstance(results[0][0], int): 
        capacity.append((int) (results[0][0]))

# HENTE NY(TT) ORDRENUMMER/BILLETTID

dager = ['Mandag', 'Tirsdag', 'Onsdag', 'Torsdag', 'Fredag', 'Lørdag', 'Søndag']
def ukedag(dato):
    dateObj= datetime.datetime.strptime(dato, '%d.%m.%Y')
    ukedagsnummer = dateObj.weekday()
    return dager[ukedagsnummer]

def new_TicketID():
    con = sqlite3.connect("sql/tog.db")
    cursor = con.cursor()
    cursor.execute(f"SELECT MAX(BillettID) FROM Billett;")
    results = cursor.fetchall()
    con.close()
    return 1 if results[0][0] == None else results[0][0]+1

def hent_delstrekning():
    con = sqlite3.connect("sql/tog.db")
    cursor = con.cursor()
    cursor.execute(f"select DelstrekningID as targetDelstrekning from Delstrekning where Delstrekning.StartStasjon = :start and Delstrekning.Endestasjon = :slutt;",
                   {"start": start,
                    "slutt": slutt})
    results = cursor.fetchall()
    con.close()
    return results[0][0]

def hent_forekomstID():
    con = sqlite3.connect("sql/tog.db")
    cursor = con.cursor()
    cursor.execute(f"select ForekomstID from TogruteForekomst where TogruteID = :togrute and Ukedag = :ukedag",
                   {"togrute": togrute,
                    "ukedag": ukedag})
    results = cursor.fetchall()
    con.close()
    
    return results[0][0]

def hent_avgangsTid():
    con = sqlite3.connect("sql/tog.db")
    cursor = con.cursor()
    cursor.execute(f"Select AvgangsTid from RuteInnom Where TogruteID = :togrute AND Stasjonsnavn = :start",
                   {"togrute": togrute,
                    "start": start})
    results = cursor.fetchall()
    con.close()
    print(results)
    return results[0][0]
    

def velg_vogn():
    if  togrute == 'Trondheim-Bodø-nattog':
        vogn = 'SJ-sovevogn-1'
    else:
        vogn = 'SJ-sittevogn-1'
    return vogn

# BESTILLE BILETTER

def fullfør_bestilling(antall_plasser):
    vogn = velg_vogn()
    forekomstID = (str) (hent_forekomstID())
    TicketID = (str) (new_TicketID())
    delstrekning = (int) ( hent_delstrekning())
    tid = (str) (hent_avgangsTid())
    con = sqlite3.connect("sql/tog.db")
    cursor = con.cursor()
    cursor.execute(f"""insert into KundeOrdre (OrdreNummer, Dag, Tid, Kundenummer) 
                    values (:userID, date('now'), time('now'), :kundenummer);""",
                    {"userID": TicketID,
                     "kundenummer": kundenummer})
    
    cursor.execute(f"""insert into Billett (BillettID, Ordrenummer, DelstrekningID, VognNavn) 
                    values (:userID, :userID, :delstrekning, :vogn)""",
                    {"userID": TicketID,
                     "delstrekning": delstrekning,
                     "vogn": vogn});
    
    cursor.execute(f"""insert into HarPlass (BillettID, Plasser, ForekomstID) 
                    values (:userID, :antall_plasser, :forekomstID)""",
                    {"userID": TicketID,
                     "antall_plasser": antall_plasser,
                     "forekomstID": forekomstID});

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

def beregn_ledige_plasser():
    con = sqlite3.connect("sql/tog.db)")
    cursor = con.cursor()
    cursor.execute(f""""
    
    With AntallSeter AS (
	SELECT  VognType.VognNavn, VognType.AntallRader*VognType.AntallSeterPerRad AS TotalSeter
	FROM TogRute 
    JOIN Oppsett on Oppsett.TogruteID = TogRute.TogruteID
    JOIN VognType on Oppsett.VognNavn = VognType.VognNavn
    WHERE VognType.VognType = (:vogntype) {"vogntype": vogn_type}
    AND TogRute.TogruteID = (:togrute) {"togrute": togrute}
	
	SELECT SUM(TotalSeter)
	FROM AntallSeter;
    """)



# KUNDESPØRRINGER
kundenummer=input("Legg inn kundenummer: ")
togrute = togruter[int(input("Velg togrute: \n (1) Trondheim-Bodø-dagtog \n (2) Trondheim-Bodø-nattog \n (3) Mo i Rana-Trondheim-morgentog \n Togrute: "))]
start=input("Startstasjon: ")
slutt=input("Sluttstasjon: ")
reisedato = input("Hvilken dato vil du reise på? ")
ukedag= ukedag(reisedato)

capacity = []
for i in set_checks(togrute):
    check_avail(i)

if togrute == 'Trondheim-Bodø-nattog':
    vogn_typer = [0, 1, 2]
    vogn_type = vogn_typer[input("Ønsker du (1) Sittevogn eller (2) Sovevogn? ")]


if bool(capacity) == False:
    print(f"Det er {10} ledige plasser på denne reisen.")
    antall_plasser=input("Hvor mange plasser ønsker du å bestille? ")
    if (int) (antall_plasser) <= 10:
        fullfør_bestilling(antall_plasser)    
else:
    print(f"Det er {10 - max(capacity)} ledige plasser på denne reisen.")
    if max(capacity) < 10:
        antall_plasser=input("Hvor mange plasser ønsker du å bestille? ")
        if (int) (antall_plasser) + max(capacity) <= 10:
            fullfør_bestilling(antall_plasser)    

