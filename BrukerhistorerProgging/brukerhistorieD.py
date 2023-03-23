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
cursor.execute(f"Select DISTINCT Togrute.TogruteID , TogruteForekomst.Ukedag from Togrute\
                join TogruteForekomst ON (TogruteForekomst.TogruteID = TogRute.TogruteID) \
                join RuteInnom ON ( TogRute.TogruteID = RuteInnom.TogruteID) \
                where (((Ukedag == '{ukedag(dato)}' AND (TogRute.AvgangsTid >= '{klokkeslett}' \
                OR RuteInnom.AvgangsTid >= '{klokkeslett}')) OR Ukedag == '{nesteukedag(dato)}')) \
                and ((TogRute.StartStasjon = '{startStasjon}' and TogRute.EndeStasjon = '{sluttStasjon}') \
                OR (TogRute.StartStasjon = '{startStasjon}' AND RuteInnom.Stasjonsnavn = '{sluttStasjon}') \
                OR (TogRute.EndeStasjon = '{sluttStasjon}' AND RuteInnom.Stasjonsnavn = '{startStasjon}'))\
                Order by TogRute.AvgangsTid, RuteInnom.AvgangsTid, TogruteForekomst.Ukedag ASC;")
results = cursor.fetchall()

def FormaterSvar():
    s = (f"Togruter som går mellom {startStasjon} og {sluttStasjon} er: \n")
    for i in range(0,len(results)):
        s += (f"{results[i][0]}  Dag: {results[i][1]}\n")
    return s

print(FormaterSvar())
con.close()
