#For en stasjon som oppgis, 
#skal bruker få ut alle togruter 
#som er innom stasjonen en gitt ukedag. 
#Denne funksjonaliteten skal programmeres.

import sqlite3
con = sqlite3.connect("tog.db")
cursor = con.cursor()
stasjon = input("Hvilken stasjon vil du ha togruter for?").lower()
ukedag = input("Hvilken ukedag ønsker du å sjekke?").lower()
cursor.execute(f"SELECT TogruteID \
               FROM TogRute JOIN TogruteForekomst ON TogRute.TogruteID = TogruteForekomst.TogruteID \
               JOIN RuteInnom ON  RuteInnom.TogruteID = TogRute.TogruteID\
               JOIN Jernbanestasjon ON Jernbanestasjon.Stasjonsnavn = RuteInnom.Stasjonsnavn\
               WHERE dag='{ukedag}' AND stasjonsnavn='{stasjon} ")
con.close()
