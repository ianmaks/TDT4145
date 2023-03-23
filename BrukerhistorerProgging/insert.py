#Denne filen skal slettes
import sqlite3
con = sqlite3.connect("sql/tog.db")
cursor = con.cursor()
#cursor.execute(f"INSERT INTO KundeOrdre (Ordrenummer, Dag, Tid, KundeNummer) \
#                VALUES (5, '2023-04-21', '07:31:00',2);")
#
#cursor.execute(f"INSERT INTO Billett (BillettID, Ordrenummer, DelstrekningID, VognNavn) \
#                VALUES (5, 5, 6, 'SJ-sittevogn-1');")
#
#cursor.execute(f"INSERT INTO HarPlass (BillettID, Plasser, ForekomstID) \
#                VALUES (5, 1, 'tro-bod-dag-man');")


cursor.execute(f"UPDATE KundeOrdre Set Dag = '2023-03-21' Where Ordrenummer = 5; ")

con.commit()
con.close()