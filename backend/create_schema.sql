CREATE TABLE IF NOT EXISTS t_art_objects (
    ArtObject TEXT PRIMARY KEY,
    ArtObjectLabel TEXT,
    ArtObjectDescription TEXT,
    OwnedBy TEXT,
    OwnedByLabel TEXT,
    CreationDate DATE, 
    Artist TEXT,
    ArtistLabel TEXT
);

CREATE TABLE IF NOT EXISTS t_art_owners (
    ArtObject TEXT REFERENCES t_art_objects(ArtObject),
    OwnerID TEXT,
    OwnerName TEXT,
    OwnershipFrom DATE, 
    OwnershipUntil DATE, 
    OwnerDescription TEXT,
    OwnerType TEXT,
    AcquisitionMethod TEXT,
    PRIMARY KEY (ArtObject, OwnerID)
);