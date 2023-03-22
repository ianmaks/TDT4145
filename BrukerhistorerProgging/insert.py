##import sqlite3
##con = sqlite3.connect("sql/tog.db")
##cursor = con.cursor()
##cursor.execute(f"INSERT INTO KundeOrdre (Ordrenummer, Dag, Tid, KundeNummer) \
##                VALUES (3, 2023-04-20, 07:20:00,3);")
##
##cursor.execute(f"INSERT INTO Billett (BillettID, Ordrenummer, DelstrekningID, VognNavn) \
##                VALUES (3, 3, 10, SJ-sittevogn-1);")
##
##con.commit()
##con.close()