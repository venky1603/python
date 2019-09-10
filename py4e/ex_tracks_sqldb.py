#Ex SQLite Creating Tracks Database
import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('tracksdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER,
    rating INTEGER,
    count INTEGER
);
''')

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
# Method to parse the third-level dictionary and get the key value
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

valid = None
while valid == None:
    fileName = input('Enter file name: ')
    try:
        parsedFile = ET.parse(fileName)
        valid = 1

        all = parsedFile.findall('dict/dict/dict')
        print('Dict count:', len(all))

        for entry in all:
            if ( lookup(entry, 'Track ID') is None ) : continue

            name = lookup(entry, 'Name')
            artist = lookup(entry, 'Artist')
            genre = lookup(entry, 'Genre')
            album = lookup(entry, 'Album')
            count = lookup(entry, 'Play Count')
            rating = lookup(entry, 'Rating')
            length = lookup(entry, 'Total Time')

            if name is None or artist is None or genre is None or album is None : continue

            print(name, artist, genre, album, count, rating, length)

            cur.execute('''INSERT OR IGNORE INTO Artist (name)
                VALUES ( ? )''', ( artist, ) )
            cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
            artist_id = cur.fetchone()[0]

            cur.execute('''INSERT OR IGNORE INTO Genre (name)
                VALUES ( ? )''', ( genre, ) )
            cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
            genre_id = cur.fetchone()[0]

            cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
                VALUES ( ?, ? )''', ( album, artist_id ) )
            cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
            album_id = cur.fetchone()[0]

            cur.execute('''INSERT OR REPLACE INTO Track
                (title, album_id, genre_id, len, rating, count)
                VALUES ( ?, ?, ?, ?, ?, ? )''',
                ( name, album_id, genre_id, length, rating, count ) )

        conn.commit()

    except Exception as e:
        print('Enter a valid file name')
