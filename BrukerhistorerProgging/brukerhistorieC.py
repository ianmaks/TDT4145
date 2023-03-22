#For en stasjon som oppgis, 
#skal bruker få ut alle togruter 
#som er innom stasjonen en gitt ukedag. 
#Denne funksjonaliteten skal programmeres.

import sqlite3
con = sqlite3.connect("sql/tog.db")
cursor = con.cursor()
stasjon = input("Hvilken stasjon vil du ha togruter for?")
ukedag = input("Hvilken ukedag ønsker du å sjekke?")

cursor.execute(f"Select Ukedag, RuteInnom.Stasjonsnavn, TogRute.TogruteID \
               From TogruteForekomst join TogRute on (TogruteForekomst.TogruteID = TogRute.TogruteID) \
               join RuteInnom on (TogruteForekomst.TogruteID = RuteInnom.TogruteID) \
               Where Ukedag == '{ukedag}' AND RuteInnom.Stasjonsnavn == '{stasjon}';")
results = cursor.fetchall()
print(results)
con.close()
