import sqlite3



con = sqlite3.connect("tog.db")
cursor = con.cursor()
startStasjon= input("Startstasjon: ")
sluttStasjon= input("Sluttstasjon: ")
dato= input("dato: ")
klokkeslett= input("klokkeslett: ")
cursor.execute(f"SELECT TogruteID \
               FROM TogRute JOIN TogruteForekomst ON TogRute.TogruteID = TogruteForekomst.TogruteID \
               JOIN RuteInnom ON  RuteInnom.TogruteID = TogRute.TogruteID\
               JOIN Jernbanestasjon ON Jernbanestasjon.Stasjonsnavn = RuteInnom.Stasjonsnavn\
               WHERE dag='{ukedag}' AND stasjonsnavn='{stasjon} ")
con.close()