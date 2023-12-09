CREATE TABLE IF NOT EXISTS t_art_objects (
    ArtObjectID TEXT PRIMARY KEY,
    ArtObjectName TEXT,
    ArtObjectDescription TEXT,
    OwnedByID TEXT,
    OwnedByName TEXT,
    ImageURL TEXT,
    CreatorName TEXT,
    DateOfCreation TEXT, -- Stored as TEXT to accommodate various date formats
    Material TEXT,
    Location TEXT,
    Height DECIMAL, -- Assuming height is in a consistent unit like cm or inches
    Width DECIMAL,  -- Assuming width is in a consistent unit like cm or inches
    Genre TEXT,
    Event TEXT,
    Source TEXT,
    Origin TEXT,
    Exhibition TEXT
);


CREATE TABLE IF NOT EXISTS t_art_owners (
    ArtObjectID TEXT REFERENCES t_art_objects(ID),
    OwnerID TEXT,
    OwnerName TEXT,
    OwnershipFrom TEXT, 
    OwnershipUntil TEXT, 
    OwnerDescription TEXT,
    OwnerType TEXT,
    AcquisitionMethod TEXT,
    PRIMARY KEY (ArtObjectID, OwnerID, OwnershipFrom)
);