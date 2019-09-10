#Ex SQLite Working with databases
import sqlite3

conn = sqlite3.connect('organization.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

valid = None
while valid is None:
    fileName = input('Enter file name: ')
    try:
        fileHandle = open(fileName)
        valid = 1
        for line in fileHandle:
            if not line.startswith('From: '): continue
            pieces = line.split()
            email = pieces[1]
            pos = email.find('@')
            org = email[pos+1:]
            cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
            row = cur.fetchone()
            if row is None:
                cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (org,))
            else:
                cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(org,))
        conn.commit()

        # https://www.sqlite.org/lang_select.html
        sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

        for row in cur.execute(sqlstr):
            print(str(row[0]), row[1])

        cur.close()

    except Exception as e:
        print('Enter a valid file name')
