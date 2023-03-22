#Bruker skal kunne søke etter togruter som går mellom en 
#startstasjon og en sluttstasjon, med utgangspunkt i en dato 
# og et klokkeslett. Alle ruter den samme dagen og den neste skal 
# returneres, sortert på tid. 
# Denne funksjonaliteten skal programmeres.
import sqlite3
import datetime

def ukedag(dato):
    dager = ['mandag', 'tirsdag', 'onsdag', 'torsdag', 'fredag', 'lørdag', 'søndag']

    dateObj= datetime.datetime.strptime(dato, '%d.%m.%Y')
    ukedagsnummer = dateObj.weekday()
    return dager[ukedagsnummer]

def nesteukedag(dato):
    dager = ['mandag', 'tirsdag', 'onsdag', 'torsdag', 'fredag', 'lørdag', 'søndag','mandag']

    dateObj= datetime.datetime.strptime(dato, '%d.%m.%Y')
    ukedagsnummer = dateObj.weekday()+1
    return dager[ukedagsnummer]

con = sqlite3.connect("sql/tog.db")

startStasjon= input("Startstasjon: ")
sluttStasjon= input("Sluttstasjon: ")
dato= input("dato f eks.(31.03.2023): ")
klokkeslett= input("klokkeslett: ")

cursor = con.cursor()
cursor.execute(f"Select TogRuteID, AdgangsTid from TogRute natural join TogruteForekomst where StartStasjon == "{startStasjon}" and EndeStasjon == "{sluttStasjon}" and (Dato == "{ukedag(dato)}" OR Dato == "{nesteukedag(dato)}") order by AdgangsTid;")
results = cursor.fetchall()
print(results)
con.close()