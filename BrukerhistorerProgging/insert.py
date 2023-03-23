import sqlite3
con = sqlite3.connect("sql/tog.db")
cursor = con.cursor()
#cursor.execute(f"INSERT INTO KundeOrdre (Ordrenummer, Dag, Tid, KundeNummer) \
#                VALUES (4, 2023-05-15, '08:11:00' ,1);")
#
#cursor.execute(f"INSERT INTO Billett (BillettID, Ordrenummer, DelstrekningID, VognNavn) \
#                VALUES (4, 4, 4, 'SJ-sovevogn-1');")
#
#cursor.execute(f"INSERT INTO HarPlass (BillettID, Plasser, ForekomstID) \
#                VALUES (3, 1, 'moi-tro-mor-man');")


con.commit()
con.close()