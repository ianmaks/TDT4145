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
cursor.execute(f"Select Togrute.TogruteID, TogruteForekomst.Ukedag ,Togrute.AvgangsTid from Togrute\
                join TogruteForekomst ON (TogruteForekomst.TogruteID = TogRute.TogruteID) where \
                StartStasjon == '{startStasjon}' and EndeStasjon == '{sluttStasjon}' \
                and ((Ukedag == '{ukedag(dato)}' AND AvgangsTid >= '{klokkeslett}') OR Ukedag == '{nesteukedag(dato)}') \
                order by AvgangsTid;")
results = cursor.fetchall()
print(results)
con.close()