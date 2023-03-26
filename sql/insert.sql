insert into Jernbanestasjon (Stasjonsnavn, Moh) values 
("Trondheim", 5.1),
("Steinkjer", 3.6),
("Mosjøen", 6.8),
("Mo i Rana", 3.5),
("Fauske", 34.0),
("Bodø", 4.1);

insert into Delstrekning (DelstrekningID, Lengde, Sportype, StartStasjon, Endestasjon) values 
(1, 120, "Dobbeltspor", "Trondheim", "Steinkjer"),
(2, 400, "Enkeltspor", "Trondheim", "Mosjøen"),
(3, 490, "Enkeltspor", "Trondheim", "Mo i Rana"),
(4, 660, "Enkeltspor", "Trondheim", "Fauske"),
(5, 720, "Enkeltspor", "Trondheim", "Bodø"),
(6, 280, "Enkeltspor", "Steinkjer", "Mosjøen"),
(7, 370, "Enkeltspor", "Steinkjer", "Mo i Rana"),
(8, 540, "Enkeltspor", "Steinkjer", "Fauske"),
(9, 600, "Enkeltspor", "Steinkjer", "Bodø"),
(10, 90, "Enkeltspor", "Mosjøen", "Mo i Rana"),
(11, 260, "Enkeltspor", "Mosjøen", "Fauske"),
(12, 320, "Enkeltspor", "Mosjøen", "Bodø"),
(13, 170, "Enkeltspor", "Mo i Rana", "Fauske"),
(14, 230, "Enkeltspor", "Mo i Rana", "Bodø"),
(15, 60, "Enkeltspor", "Fauske", "Bodø"),
(16, 90, "Enkeltspor", "Mo i Rana", "Mosjøen"),
(17, 370, "Enkeltspor", "Mo i Rana", "Steinkjer"),
(18, 490, "Enkeltspor", "Mo i Rana", "Trondheim"),
(19, 280, "Enkeltspor", "Mosjøen", "Steinkjer"),
(20, 400, "Enkeltspor", "Mosjøen", "Trondheim"),
(21, 120, "Dobbeltspor", "Steinkjer", "Trondheim");


insert into Banestrekning (Banestrekningnavn, Start, Slutt, Fremdriftsenergi) values
("Trondheim-Bodø", "Trondheim", "Bodø", "Diesel");

insert into BestårAv (BanestrekningNavn, DelstrekningID) values
("Trondheim-Bodø", 1),
("Trondheim-Bodø", 2),
("Trondheim-Bodø", 3),
("Trondheim-Bodø", 4),
("Trondheim-Bodø", 5),
("Trondheim-Bodø", 6),
("Trondheim-Bodø", 7),
("Trondheim-Bodø", 8),
("Trondheim-Bodø", 9),
("Trondheim-Bodø", 10),
("Trondheim-Bodø", 11),
("Trondheim-Bodø", 12),
("Trondheim-Bodø", 13),
("Trondheim-Bodø", 14),
("Trondheim-Bodø", 15);

insert into StrekningInnom (DelstrekningID, Stasjonsnavn) values
(2, "Mosjøen"),
(3, "Steinkjer"),
(3, "Mosjøen"),
(4, "Steinkjær"),
(4, "Mosjøen"),
(4, "Mo i Rana"),
(5, "Steinkjer"),
(5, "Mosjøen"),
(5, "Mo i Rana"),
(5, "Fauske"),
(7, "Mosjøen"),
(8, "Mo i Rana"),
(8, "Fauske"),
(9, "Mosjøen"),
(9, "Mo i Rana"),
(9, "Fauske"),
(11, "Mo i rana"),
(12, "Mo i Rana"),  
(12, "Fauske"),
(14, "Fauske");

insert into TogRute (TogruteID, Operatør) values
("Trondheim-Bodø-dagtog","SJ"),
("Trondheim-Bodø-nattog", "SJ"),
("Mo i Rana-Trondheim-morgentog","SJ");

insert into RuteInnom (TogRuteID, Stasjonsnavn, AnkomstTid, AvgangsTid, Indeks) values
("Trondheim-Bodø-dagtog", "Trondheim", NULL, "07:49:00", 0),
("Trondheim-Bodø-dagtog", "Steinkjer", "09:49:00", "09:51:00", 1),
("Trondheim-Bodø-dagtog", "Mosjøen", "13:18:00", "13:20:00", 2),
("Trondheim-Bodø-dagtog", "Mo i Rana", "14:29:00", "14:31:00", 3),
("Trondheim-Bodø-dagtog", "Fauske", "16:47:00", "16:49:00",4),
("Trondheim-Bodø-dagtog", "Bodø", "17:34:00", NULL, 5),
("Trondheim-Bodø-nattog", "Trondheim", NULL, "23:05:00",0),
("Trondheim-Bodø-nattog", "Steinkjer", "00:55:00", "00:57:00",1),
("Trondheim-Bodø-nattog", "Mosjøen", "04:39:00", "04:41:00",2),
("Trondheim-Bodø-nattog", "Mo i Rana", "05:53:00", "05:55:00",3),
("Trondheim-Bodø-nattog", "Fauske", "08:17:00", "08:19:00",4),
("Trondheim-Bodø-nattog", "Bodø","09:05:00", NULL,5),
("Mo i Rana-Trondheim-morgentog", "Mo i Rana", NULL, "08:11:00",0),
("Mo i Rana-Trondheim-morgentog", "Mosjøen", "09:12:00", "09:14:00",1),
("Mo i Rana-Trondheim-morgentog", "Steinkjer", "12:29:00", "12:31:00",2),
("Mo i Rana-Trondheim-morgentog", "Trondheim", "14:13:00",NULL,3);

insert into TogruteForekomst (ForekomstID, Ukedag, TogruteID) values
("tro-bod-dag-man", "Mandag", "Trondheim-Bodø-dagtog"),
("tro-bod-dag-tir", "Tirsdag", "Trondheim-Bodø-dagtog"),
("tro-bod-dag-ons", "Onsdag", "Trondheim-Bodø-dagtog"),
("tro-bod-dag-tor", "Torsdag", "Trondheim-Bodø-dagtog"),
("tro-bod-dag-fre", "Fredag", "Trondheim-Bodø-dagtog"),

("tro-bod-nat-man", "Mandag", "Trondheim-Bodø-nattog"),
("tro-bod-nat-tir", "Tirsdag", "Trondheim-Bodø-nattog"),
("tro-bod-nat-ons", "Onsdag", "Trondheim-Bodø-nattog"),
("tro-bod-nat-tor", "Torsdag", "Trondheim-Bodø-nattog"),
("tro-bod-nat-fre", "Fredag", "Trondheim-Bodø-nattog"),
("tro-bod-nat-lør", "Lørdag", "Trondheim-Bodø-nattog"),
("tro-bod-nat-søn", "Søndag", "Trondheim-Bodø-nattog"),

("moi-tro-mor-man", "Mandag", "Mo i Rana-Trondheim-morgentog"),
("moi-tro-mor-tir", "Tirsdag", "Mo i Rana-Trondheim-morgentog"),
("moi-tro-mor-ons", "Onsdag", "Mo i Rana-Trondheim-morgentog"),
("moi-tro-mor-tor", "Torsdag", "Mo i Rana-Trondheim-morgentog"),
("moi-tro-mor-fre", "Fredag", "Mo i Rana-Trondheim-morgentog"),
("moi-tro-mor-lør", "Lørdag", "Mo i Rana-Trondheim-morgentog"),
("moi-tro-mor-søn", "Søndag", "Mo i Rana-Trondheim-morgentog");

insert into VognType (VognType, VognNavn, AntallRader, AntallSeterPerRad, AntallKupeer) values
(1, "SJ-sittevogn-1", 3, 4, NULL),
(1, "SJ-sittevogn-2", 3, 4, NULL),
(1, "SJ-sittevogn-3", 3, 4, NULL),
(1, "SJ-sittevogn-4", 3, 4, NULL),
(2, "SJ-sovevogn-1", NULL, NULL, 4);

insert into Oppsett(VognNavn, TogRuteID) values
("SJ-sittevogn-1", "Trondheim-Bodø-dagtog"),
("SJ-sittevogn-2", "Trondheim-Bodø-dagtog"),
("SJ-sittevogn-3","Trondheim-Bodø-nattog"),
("SJ-sovevogn-1","Trondheim-Bodø-nattog"),
("SJ-sittevogn-4","Mo i Rana-Trondheim-morgentog");



/* Ekstra innsetting for å kunne teste brukerhistoriene*/


insert into Kunde(Kundenummer, Navn, Epost, Mobilnummer) values
(1, "Ola Nordmann", "ola.nordmann@gmail.com", "40482387"),
(2, "Mari sivertsen", "mari_sivertsen@hotmail.com", "99785476"),
(3, "Lise Johansen", "lissieLovesHorses@yahoo.com", "99703644"),
(4, "Johanne Bø", "johbo@gmail.com", "40457676");

insert into KundeOrdre(OrdreNummer, Dag, Tid, Kundenummer) values
(1, "2023-04-04", "07:40:00", 1),
(2, "2023-03-29", "09:51:00", 2),
(3, "2023-04-20", "23:05:00", 1),
(4, "2023-05-12", "08:11:00", 3),
(5, "2023-03-20", "09:51:00", 2),
(6, "2023-03-31", "13:20:00", 1),
(7, "2023-04-12", "13:20:00", 3),
(8, "2023-03-29", "13:20:00", 4);

insert into Billett(BillettID, OrdreNummer, DelstrekningID, VognNavn) values
(1, 1, 5, "SJ-sittevogn-1"),
(2, 2, 8, "SJ-sittevogn-1"),
(3, 3, 4, "SJ-sovevogn-3"),
(4, 4, 17, "SJ-sittevogn-4"),
(5, 5, 6, "SJ-sittevogn-1"),
(6, 6, 11, "SJ-sittevogn-1"),
(7, 7, 11, "SJ-sittevogn-1"),
(8, 8, 14, "SJ-sittevogn-1");

insert into HarPlass(BillettID, Plasser, ForekomstID) values
(1, 1, "tro-bod-dag-tir"),
(2, 2, "tro-bod-dag-ons"),
(3, 1, "tro-bod-nat-tor"),
(4, 2, "moi-tro-mor-fre"),
(5, 1, "tro-bod-dag-man"),
(6, 2, "tro-bod-dag-fre"),
(7, 2, "tro-bod-dag-ons"),
(8, 2, "tro-bod-dag-ons");

