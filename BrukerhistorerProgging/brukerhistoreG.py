#Registrerte kunder skal kunne finne ledige billetter for en oppgitt strekning på en ønsket togrute og kjøpe de billettene hen ønsker. Denne funksjonaliteten skal programmeres.
#Pass på at dere bare selger ledige plasser
import sqlite3
con = sqlite3.connect("tog.db")
cursor = con.cursor()
cursor.execute(f"")
con.close()