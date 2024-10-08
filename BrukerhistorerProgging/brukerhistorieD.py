#Bruker skal kunne søke etter togruter som går mellom en 
#startstasjon og en sluttstasjon, med utgangspunkt i en dato 
# og et klokkeslett. Alle ruter den samme dagen og den neste skal 
# returneres, sortert på tid. 
# Denne funksjonaliteten skal programmeres.
import sqlite3
import datetime

dager = ['Mandag', 'Tirsdag', 'Onsdag', 'Torsdag', 'Fredag', 'Lørdag', 'Søndag']
def ukedag(dato):
    dateObj= datetime.datetime.strptime(dato, '%d.%m.%Y')
    ukedagsnummer = dateObj.weekday()
    return dager[ukedagsnummer]

def nesteukedag(dato):
    dagene = ['Mandag', 'Tirsdag', 'Onsdag', 'Torsdag', 'Fredag', 'Lørdag', 'Søndag', "Mandag"]
    dateObj= datetime.datetime.strptime(dato, '%d.%m.%Y')
    ukedagsnummer = dateObj.weekday()+1
    return dagene[ukedagsnummer]

def sortedbytime(results):  
    out=[]
    results.sort(key=lambda x: x[2])
    for k in dager:
        for i in results:
            out.append(i) if i[1]==k else None
    return out


def FormaterSvar(results):
    results=sortedbytime(results)
    s = (f"Togruter som går mellom {startStasjon} og {sluttStasjon} er: \n")
    for i in range(0,len(results)):
        s += (f"{results[i][0]}  Dag: {results[i][1]} Tid: {results[i][2]}\n")

    if len(results)==0:
        return (f"Ingen togreiser går mellom {startStasjon} og {sluttStasjon} i denne tidsperioden")
    return s

con = sqlite3.connect("tog.db")

startStasjon= input("Startstasjon: ")
sluttStasjon= input("Sluttstasjon: ")
dato= input("dato f eks.(31.03.2023): ")
klokkeslett= input("klokkeslett f eks. (07:49:00): ")

cursor = con.cursor()
cursor.execute(f"""SELECT DISTINCT Togrute.TogruteID, TogruteForekomst.Ukedag,  RuteInnomStart.AvgangsTid
                FROM Togrute 
                
                JOIN TogruteForekomst 
                ON (TogruteForekomst.TogruteID = TogRute.TogruteID) 
                
                JOIN (Select * From RuteInnom) RuteInnomSlutt
                ON (TogRute.TogruteID = RuteInnomSlutt.TogruteID) 

                JOIN (Select * From RuteInnom) RuteInnomStart
                ON (TogRute.TogruteID = RuteInnomStart.TogruteID) 
                
                WHERE ((Ukedag = :ukedag AND (RuteInnomStart.AvgangsTid >= :klokkeslett) OR Ukedag = :nesteukedag)
                AND (RuteInnomStart.Stasjonsnavn = :startStasjon AND RuteInnomSlutt.Stasjonsnavn = :sluttStasjon)
                AND (RuteInnomStart.Indeks < RuteInnomSlutt.Indeks))
                ;""", 
                {"klokkeslett": klokkeslett,
                 "ukedag": ukedag(dato),
                 "nesteukedag": nesteukedag(dato),
                 "startStasjon": startStasjon,
                 "sluttStasjon": sluttStasjon
                 })
results = cursor.fetchall()

print(FormaterSvar(results))
con.close()

