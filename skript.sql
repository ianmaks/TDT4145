CREATE TABLE Jernbanestasjon (
    Stasjonsnavn varchar(255) NOT NULL,
    moh float,
    PRIMARY KEY (StasjonsNavn)
);

CREATE TABLE TogRute (
    ID int NOT NULL,
    Startstasjon varchar(255) NOT NULL,
    Endestasjon varchar(255) NOT NULL,
    Operatør varchar(255) NOT NULL,
    AdgangsTid datetime,
    AnkomstTid datetime,
    CONSTRAINT PK PRIMARY KEY (ID),
    CONSTRAINT FK1 FOREIGN KEY (Startstasjon) REFERENCES Jernbanestasjon(Stasjonsnavn)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    CONSTRAINT FK2 FOREIGN KEY (Endestasjon) REFERENCES Jernbanestasjon(Stasjonsnavn)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE VognType (
    Navn varchar(255) NOT NULL,
    antallRader int,
    antallSeterPerRad int,
    antallKupeer int,
    CONSTRAINT PK PRIMARY KEY (Navn)
);

CREATE TABLE Banestrekning (
    Navn varchar(255) NOT NULL,
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
    ID int NOT NULL,
    StartStasjon varchar(255) NOT NULL,
    Endestasjon varchar(255) NOT NULL,
    lengde float,
    Sportype varchar(255),
    CONSTRAINT PK PRIMARY KEY (ID),
    CONSTRAINT FK1 FOREIGN KEY (StartStasjon) REFERENCES Jernbanestasjon(Stasjonsnavn)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    CONSTRAINT FK2 FOREIGN KEY (Endestasjon) REFERENCES Jernbanestasjon(Stasjonsnavn)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE BestårAv (
    Navn varchar(255) NOT NULL,
    ID int NOT NULL,
    CONSTRAINT PK PRIMARY KEY (Navn, ID),
    CONSTRAINT FK1 FOREIGN KEY (Navn) REFERENCES Banestrekning(Navn)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    CONSTRAINT FK2 FOREIGN KEY (ID) REFERENCES Delstrekning(ID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE Kunde (
    Kundenummer int NOT NULL,
    navn varchar(255) NOT NULL,
    epost varchar(255) NOT NULL,
    mobilnummer varchar(255) NOT NULL,
    CONSTRAINT PK PRIMARY KEY (Kundenummer)
);

CREATE TABLE TogruteForekomst (
    TogruteID int NOT NULL,
    Dag datetime NOT NULL,
    CONSTRAINT PK PRIMARY KEY (TogruteID, Dag)
);

CREATE TABLE KundeOrdre (
    OrdreNummer int NOT NULL,
    Dag datetime NOT NULL,
    Tid datetime NOT NULL,
    Kundenummer int NOT NULL,
    CONSTRAINT PK PRIMARY KEY (OrdreNummer),
    CONSTRAINT FK FOREIGN KEY (Kundenummer) REFERENCES Kunde(Kundenummer)
    ON UPDATE CASCADE 
);

CREATE TABLE Billett (
    BillettID int NOT NULL,
    ordrenummer int NOT NULL,
    DelstrekningID int NOT NULL,
    VognNavn varchar(255),
    CONSTRAINT PK PRIMARY KEY (BillettID),
    CONSTRAINT FK1 FOREIGN KEY (ordrenummer) REFERENCES KundeOrdre(OrdreNummer)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    CONSTRAINT FK2 FOREIGN KEY (DelstrekningID) REFERENCES Delstrekning(ID)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    CONSTRAINT FK3 FOREIGN KEY (VognNavn) REFERENCES VognType(Navn)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE HarPlass (
    BillettID int NOT NULL,
    plasser int NOT NULL,
    ForekomstID int NOT NULL,
    CONSTRAINT PK PRIMARY KEY (BillettID),
    CONSTRAINT FK1 FOREIGN KEY (BillettID) REFERENCES Billett(BillettID)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    CONSTRAINT FK2 FOREIGN KEY (ForekomstID) REFERENCES TogruteForekomst(ForekomstID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);
