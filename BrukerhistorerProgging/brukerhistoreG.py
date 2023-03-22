#Registrerte kunder skal kunne finne ledige billetter for en oppgitt strekning på en ønsket togrute 
#og kjøpe de billettene hen ønsker.
#
#Pass på at dere bare selger ledige plasser
import sqlite3

kundenummer=input("Legg inn kundenummer: ")
start=input("Startstasjon: ")
slutt=input("Sluttstasjon: ")

con = sqlite3.connect("python/TDT4145_prosjekt/sql/tog.db")
cursor = con.cursor()
cursor.execute(f"")

kjope=input("angi hvilken du ønsker å kjøpe")
con.close()