#For en stasjon som oppgis, 
#skal bruker få ut alle togruter 
#som er innom stasjonen en gitt ukedag. 
#Denne funksjonaliteten skal programmeres.


import sqlite3
con = sqlite3.connect("tog.db")
cursor = con.cursor()
stasjon = input("Hvilken stasjon vil du ha togruter for?")
ukedag = input("Hvilken ukedag ønsker du å sjekke?")

cursor.execute(f"""Select DISTINCT TogRute.TogruteID 
               From TogruteForekomst JOIN TogRute 
               ON (TogruteForekomst.TogruteID = TogRute.TogruteID)
               JOIN RuteInnom ON 
               (TogruteForekomst.TogruteID = RuteInnom.TogruteID)
               WHERE 
               Ukedag == :ukedag AND RuteInnom.Stasjonsnavn == :stasjon;"""
               ,{"ukedag": ukedag,"stasjon": stasjon})
               
results = cursor.fetchall()

def FormatertSvar():
    s = (f"Togruter som er gjennom {stasjon} på {ukedag}: \n")
    for i in range(0,len(results)):
        s += (f"{results[i][0]}\n")
    return s

print(FormatertSvar())
con.close()
