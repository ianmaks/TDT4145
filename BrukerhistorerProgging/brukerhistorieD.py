#Bruker skal kunne søke etter togruter som går mellom en 
#startstasjon og en sluttstasjon, med utgangspunkt i en dato 
# og et klokkeslett. Alle ruter den samme dagen og den neste skal 
# returneres, sortert på tid. 
# Denne funksjonaliteten skal programmeres.
import sqlite3

con = sqlite3.connect("tog.db")
cursor = con.cursor()
startStasjon= input("Startstasjon: ")
sluttStasjon= input("Sluttstasjon: ")
dato= input("dato: ")
klokkeslett= input("klokkeslett: ")
#denne spørringen er gal
cursor.execute(f"")
con.close()