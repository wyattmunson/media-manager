CREATE TYPE content_types AS ENUM ('movie', 'tv', 'miniseries', 'unknown');
CREATE TABLE titles (
    "titleId"   SERIAL PRIMARY KEY,
    name        VARCHAR,
    type        content_types,
    "imdbId"    VARCHAR
);

CREATE TYPE resolution_sizes AS ENUM ('480', '720', '1080', '2K', '4K', 'unknown');
CREATE TYPE status_types AS ENUM ('pending', 'ripping', 'ripped', 'transcoding', 'transcoded', 'saved', 'error');

CREATE TABLE content (
    "contentId" SERIAL PRIMARY KEY,
    "titleId"   INTEGER REFERENCES titles ("titleId"),
    season      INTEGER,
    status      status_types,
    resolution  resolution_sizes,
    "fileName"  VARCHAR,
    "MIA"       BOOLEAN,
    "NRT"       BOOLEAN,
    "EZE"       BOOLEAN,
    "CHO"       BOOLEAN
);

CREATE TYPE disk_types AS ENUM ('dvd', 'bluray');

CREATE TABLE rips (
    "ripId"         SERIAL PRIMARY KEY,
    "collectionId"  INTEGER REFERENCES collections ("collectionId"),
    "disk"          INTEGER,
    "diskType"      disk_types,
    "fileName"      VARCHAR,
    status          status_types,
    season          INTEGER
);