#Bruker skal kunne søke etter togruter som går mellom en 
#startstasjon og en sluttstasjon, med utgangspunkt i en dato 
# og et klokkeslett. Alle ruter den samme dagen og den neste skal 
# returneres, sortert på tid. 
# Denne funksjonaliteten skal programmeres.
import sqlite3

def nextDay(dato):
    dato = dato.split(".")
    dato[0] = int(dato[0]) + 1
    return ".".join(dato)

con = sqlite3.connect("tog.db")

startStasjon= input("Startstasjon: ")
sluttStasjon= input("Sluttstasjon: ")
dato= input("dato f eks.(31.03.2023): ")
klokkeslett= input("klokkeslett: ")

cursor = con.cursor()
cursor.execute(f"Select TogRuteID, AdgangsTid from TogRute
                natural join TogruteForekomst \
                where StartStasjon == "{startStasjon}" \
                and EndeStasjon == "{sluttStasjon}" \
                and (Dato == "{dato}" OR Dato == "{dato}"+1) order by AdgangsTid;")
con.close()