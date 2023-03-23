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

insert into TogRute (TogruteID, StartStasjon, EndeStasjon, Operatør, AvgangsTid, AnkomstTid) values
("Trondheim-Bodø-dagtog","Trondheim", "Bodø", "SJ", "07:49:00", "17:34:00"),
("Trondheim-Bodø-nattog", "Trondheim", "Bodø", "SJ", "23:05:00", "09:05:00"),
("Mo i Rana-Trondheim-morgentog","Mo i Rana", "Trondheim",  "SJ", "08:11:00", "14:13:00");

insert into RuteInnom (TogRuteID, Stasjonsnavn, AnkomstTid, AvgangsTid) values
("Trondheim-Bodø-dagtog", "Steinkjer", "09:49:00", "09:51:00"),
("Trondheim-Bodø-dagtog", "Mosjøen", "13:18:00", "13:20:00"),
("Trondheim-Bodø-dagtog", "Mo i Rana", "14:29:00", "14:31:00"),
("Trondheim-Bodø-dagtog", "Fauske", "16:47:00", "16:49:00"),
("Trondheim-Bodø-nattog", "Steinkjer", "00:55:00", "00:57:00"),
("Trondheim-Bodø-nattog", "Mosjøen", "04:39:00", "04:41:00"),
("Trondheim-Bodø-nattog", "Mo i Rana", "05:53:00", "05:55:00"),
("Trondheim-Bodø-nattog", "Fauske", "08:17:00", "08:19:00"),
("Mo i Rana-Trondheim-morgentog", "Mosjøen", "09:12:00", "09:14:00"),
("Mo i Rana-Trondheim-morgentog", "Steinkjer", "12:29:00", "12:31:00");

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
(2, "SJ-sovevogn-1", NULL, NULL, 4);