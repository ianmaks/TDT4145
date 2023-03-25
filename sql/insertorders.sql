insert into KundeOrdre (OrdreNummer, Dag, Tid, Kundenummer) values
(6, "2023-03-26", "07:30:00", 1),
(7, "2023-03-26", "07:35:00", 2),
(8, "2023-03-26", "07:37:00", 1);

insert into Billett (BillettID, Ordrenummer, DelstrekningID, VognNavn) values
(6, 6, 11, "SJ-sittevogn-1"),
(7, 7, 11, "SJ-sittevogn-1"),
(8, 8, 14, "SJ-sittevogn-1");

insert into HarPlass (BillettID, Plasser, ForekomstID) values
(6, 2, "tro-bod-dag-ons"),
(7, 2, "tro-bod-dag-ons"),
(8, 2, "tro-bod-dag-ons");