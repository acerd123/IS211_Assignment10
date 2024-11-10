
CREATE TABLE Artist (
    artist_id INTEGER PRIMARY KEY,
    artist_name TEXT NOT NULL
);


CREATE TABLE Album (
    album_id INTEGER PRIMARY KEY,
    album_name TEXT NOT NULL,
    artist_id INTEGER,
    FOREIGN KEY (artist_id) REFERENCES Artist(artist_id)
);


CREATE TABLE Song (
    song_id INTEGER PRIMARY KEY,
    song_name TEXT NOT NULL,
    album_id INTEGER,
    track_number INTEGER,
    song_length INTEGER, 
    FOREIGN KEY (album_id) REFERENCES Album(album_id)
);

