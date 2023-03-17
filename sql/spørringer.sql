/*Spørring c
For en stasjon som oppgis, skal bruker få ut alle 
togruter som er innom stasjonen en gitt ukedag.
Denne funksjonaliteten skal programmeres.
*/


Select TogRuteID from TogRute 
Natural Join TogruteForekomst 
Natural join RuteInnom 
Natural join Jernbanestasjon
Where Jernbanestasjon.StasjonsNavn == "stasjonnavn" 
AND TogruteForekomst.Ukedag == "ukedag";

/*Spørring d
Bruker skal kunne søke etter togruter som går mellom 
en startstasjon og en sluttstasjon, med utgangspunkt i 
en dato og et klokkeslett. Alle ruter den samme dagen og 
den neste skal returneres, sortert på tid. 
Denne funksjonaliteten skal programmeres.*/

Select TogRuteID, AdgangsTid from TogRute
natural join TogruteForekomst 
where StartStasjon == "startstasjon" 
and EndeStasjon == "endestasjon"
and (Dato == "dato" OR Dato == "dato"+1)
order by AdgangsTid;


/*spørring h
For en bruker skal man kunne finne all informasjon 
om de kjøpene hen har gjort for fremtidige
reiser. Denne funksjonaliteten skal programmeres.*/

Select Ordrenummer, Dag, Tid from KundeOrdre 
natural join Billett 
natural join HarPlass
natural join TogruteForekomst
where Dato > currentDate;







