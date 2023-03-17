CREATE TABLE Jernbanestasjon (
    Stasjonsnavn varchar(255) NOT NULL,
    Moh float,
    CONSTRAINT PK PRIMARY KEY (StasjonsNavn)
);

CREATE TABLE TogRute (
    TogruteID int NOT NULL,
    Startstasjon varchar(255) NOT NULL,
    Endestasjon varchar(255) NOT NULL,
    Operatør varchar(255) NOT NULL,
    AdgangsTid time,
    AnkomstTid time,
    CONSTRAINT PK PRIMARY KEY (TogruteID),
    CONSTRAINT FK1 FOREIGN KEY (Startstasjon) REFERENCES Jernbanestasjon(Stasjonsnavn)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    CONSTRAINT FK2 FOREIGN KEY (Endestasjon) REFERENCES Jernbanestasjon(Stasjonsnavn)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE VognType (
    Navn varchar(255) NOT NULL,
    AntallRader int,
    AntallSeterPerRad int,
    AntallKupeer int,
    CONSTRAINT PK PRIMARY KEY (Navn)
);

CREATE TABLE Banestrekning (
    BanestrekningNavn varchar(255) NOT NULL,
    Start varchar(255) NOT NULL,
    Slutt varchar(255) NOT NULL,
    Fremdriftsenergi varchar(255),
    CONSTRAINT PK PRIMARY KEY (Navn),
    CONSTRAINT FK1 FOREIGN KEY (Start) REFERENCES Jernbanestasjon(Stasjonsnavn)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    CONSTRAINT FK2 FOREIGN KEY (Slutt) REFERENCES Jernbanestasjon(Stasjonsnavn)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE Delstrekning (
    DelstrekningID int NOT NULL,
    StartStasjon varchar(255) NOT NULL,
    Endestasjon varchar(255) NOT NULL,
    lengde float,
    Sportype varchar(255),
    CONSTRAINT PK PRIMARY KEY (DelstrekningID),
    CONSTRAINT FK1 FOREIGN KEY (StartStasjon) REFERENCES Jernbanestasjon(Stasjonsnavn)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    CONSTRAINT FK2 FOREIGN KEY (Endestasjon) REFERENCES Jernbanestasjon(Stasjonsnavn)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE BestårAv (
    BaneStrekningNavn varchar(255) NOT NULL,
    DelstrekningID int NOT NULL,
    CONSTRAINT PK PRIMARY KEY (BaneStrekningNavn, DelstrekningID),
    CONSTRAINT FK1 FOREIGN KEY (BaneStrekningNavn) REFERENCES Banestrekning(BaneStrekningNavn)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    CONSTRAINT FK2 FOREIGN KEY (DelstrekningID) REFERENCES Delstrekning(DelstrekningID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE Kunde (
    Kundenummer int NOT NULL,
    Navn varchar(255) NOT NULL,
    Epost varchar(255) NOT NULL,
    Mobilnummer varchar(255) NOT NULL,
    CONSTRAINT PK PRIMARY KEY (Kundenummer)
);

CREATE TABLE TogruteForekomst (
    ForekomstID int NOT NULL,
    Ukedag Varchar(255) NOT NULL,
    Dato date NOT NULL,
    TogruteID int NOT NULL,
    CONSTRAINT PK PRIMARY KEY (ForekomstID, Dato),
    CONSTRAINT FK FOREIGN KEY (TogruteID) REFERENCES TogRute(TogruteID)
    ON UPDATE CASCADE 
    ON DELETE CASCADE

);

CREATE TABLE KundeOrdre (
    OrdreNummer int NOT NULL,
    Dag date NOT NULL,
    Tid time NOT NULL,
    Kundenummer int NOT NULL,
    CONSTRAINT PK PRIMARY KEY (OrdreNummer),
    CONSTRAINT FK FOREIGN KEY (Kundenummer) REFERENCES Kunde(Kundenummer)
    ON UPDATE CASCADE 
);

CREATE TABLE Billett (
    BillettID int NOT NULL,
    Ordrenummer int NOT NULL,
    DelstrekningID int NOT NULL,
    VognNavn varchar(255),
    CONSTRAINT PK PRIMARY KEY (BillettID),
    CONSTRAINT FK1 FOREIGN KEY (Ordrenummer) REFERENCES KundeOrdre(OrdreNummer)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    CONSTRAINT FK2 FOREIGN KEY (DelstrekningID) REFERENCES Delstrekning(DelstrekningID)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    CONSTRAINT FK3 FOREIGN KEY (VognNavn) REFERENCES VognType(Navn)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE HarPlass (
    BillettID int NOT NULL,
    Plasser int NOT NULL,
    ForekomstID int NOT NULL,
    CONSTRAINT PK PRIMARY KEY (BillettID),
    CONSTRAINT FK1 FOREIGN KEY (BillettID) REFERENCES Billett(BillettID)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    CONSTRAINT FK2 FOREIGN KEY (ForekomstID) REFERENCES TogruteForekomst(ForekomstID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);


CREATE TABLE StrekningInnom(
    DelstrekningID int NOT NULL,
    Stasjonsnavn varchar(255) NOT NULL,
    CONSTRAINT PK PRIMARY KEY (DelstrekningID, StasjonsNavn),
    CONSTRAINT FK1 FOREIGN KEY (Stasjonsnavn) REFERENCES Jernbanestasjon(Stasjonsnavn)
    ON UPDATE CASCADE
    ON DELETE CASCADE
    CONSTRAINT FK2 FOREIGN KEY (DelstrekningID) REFERENCES Delstrekning(DelstrekningID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
    
);

CREATE TABLE RuteInnom(
    TogruteID int NOT NULL,
    Stasjonsnavn varchar(255) NOT NULL,
    AnkomstTid time,
    AvgangsTid time,
    CONSTRAINT PK PRIMARY KEY (TogruteID, Stasjonsnavn),
    CONSTRAINT FK1 FOREIGN KEY (TogruteID) REFERENCES Togrute(TogruteID)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    CONSTRAINT FK2 FOREIGN KEY (Stasjonsnavn) REFERENCES Jernbanestasjon(StasjonsNavn)
    ON UPDATE CASCADE
    ON DELETE CASCADE
)
