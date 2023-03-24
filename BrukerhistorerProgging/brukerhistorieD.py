#Bruker skal kunne søke etter togruter som går mellom en 
#startstasjon og en sluttstasjon, med utgangspunkt i en dato 
# og et klokkeslett. Alle ruter den samme dagen og den neste skal 
# returneres, sortert på tid. 
# Denne funksjonaliteten skal programmeres.
import sqlite3
import datetime

def ukedag(dato):
    dager = ['Mandag', 'Tirsdag', 'Onsdag', 'Torsdag', 'Fredag', 'Lørdag', 'Søndag']

    dateObj= datetime.datetime.strptime(dato, '%d.%m.%Y')
    ukedagsnummer = dateObj.weekday()
    return dager[ukedagsnummer]

def nesteukedag(dato):
    dager = ['Mandag', 'Tirsdag', 'Onsdag', 'Torsdag', 'Fredag', 'Lørdag', 'Søndag','Mandag']

    dateObj= datetime.datetime.strptime(dato, '%d.%m.%Y')
    ukedagsnummer = dateObj.weekday()+1
    return dager[ukedagsnummer]

con = sqlite3.connect("sql/tog.db")

startStasjon= input("Startstasjon: ")
sluttStasjon= input("Sluttstasjon: ")
dato= input("dato f eks.(31.03.2023): ")
klokkeslett= input("klokkeslett f eks. (07:49:00): ")

cursor = con.cursor()
cursor.execute(f"""SELECT DISTINCT Togrute.TogruteID, TogruteForekomst.Ukedag
                FROM Togrute 
                JOIN TogruteForekomst ON (TogruteForekomst.TogruteID = TogRute.TogruteID) 
                JOIN ( 
                SELECT RuteInnom.Stasjonsnavn, RuteInnom.TogruteID, RuteInnom.AvgangsTid 
                FROM RuteInnom 
                ) RuteInnomStart ON (TogRute.TogruteID = RuteInnomStart.TogruteID) 
                JOIN ( 
                SELECT RuteInnom.Stasjonsnavn, RuteInnom.TogruteID 
                FROM RuteInnom
                ) RuteInnomSlutt ON (TogRute.TogruteID = RuteInnomSlutt.TogruteID)
                WHERE ((
                (Ukedag = :ukedag AND (TogRute.AvgangsTid >= :klokkeslett OR RuteInnomStart.AvgangsTid >= :klokkeslett)) 
                OR Ukedag = :nesteukedag)
                AND ((TogRute.StartStasjon = :startStasjon AND TogRute.EndeStasjon = :sluttStasjon)
                OR (TogRute.StartStasjon = :startStasjon AND RuteInnomSlutt.Stasjonsnavn = :sluttStasjon)
                OR (TogRute.EndeStasjon = :sluttStasjon AND RuteInnomStart.Stasjonsnavn = :startStasjon)
                OR (RuteInnomStart.Stasjonsnavn = :startStasjon AND RuteInnomSlutt.Stasjonsnavn = :sluttStasjon 
                AND RuteInnomStart.TogruteID = RuteInnomSlutt.TogruteID 
                )))
                ORDER BY TogRute.AvgangsTid, RuteInnomStart.AvgangsTid;""", 
                {"klokkeslett": klokkeslett,
                 "ukedag": ukedag(dato),
                 "nesteukedag": nesteukedag(dato),
                 "startStasjon": startStasjon,
                 "sluttStasjon": sluttStasjon,
                 })
results = cursor.fetchall()



def FormaterSvar():
    s = (f"Togruter som går mellom {startStasjon} og {sluttStasjon} er: \n")
    f = []
    i = 0
    #Luker ut feilen der mellomstasjoner i Mo i Rana-Trondheim-morgentog inkluderer alle togreiser
    for i in range(0,len(results)):
        if('Mo i Rana-Trondheim-morgentog' in results[i]):
            f.append(results[i])
            i+=1
    if f:
        for i in range(0, len(f)):
            s += (f"{f[i][0]}  Dag: {f[i][1]}  \n")
            i+=1
        return s
    #alle andre tilfeller
    for i in range(0,len(results)):
        s += (f"{results[i][0]}  Dag: {results[i][1]}\n")

    if (i==0):
        return (f"Der var det visst ingen togruter som gikk")
    return s




print(FormaterSvar())
con.close()


