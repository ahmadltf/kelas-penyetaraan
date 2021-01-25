#ahamd luthfi hanif, tutorial 12

import sqlite3

conn = sqlite3.connect("db,db")
c = conn.cursor()

c.execute("DROP TABLE IF EXIST tab")
c.execute("""CREATE TABLE tab
        (nama, text,
        usia INT(255),
        email text)
""")
#c.execute("INSERT INTO tab VALUES ('lutfi',11,'ayaya@gmail.com')")
listdata=[
    ('nama',23,'nini@gmail.com'),
    ('nama',31,'gaga@gmail.com'),
    ('nico',22,'dodo@gmail.com'),
    ('fawaz',12,'wawas@gmail.com')
]
c.executemany('INSERT INTO TAB VALUES (?,?,?)',listdata)
c.execute('UPDATE tab SET nama='fawaz', umur=32 WHERE rowid=5')
c.execute('DELETE FROM tab WHERE rowid==5')
c.execute('SELECT rowid,*FROM tab')

items=c.fetchall()

for f in items:
    print(f)

c.execute('''create table gambar
        (gambar BLOB)
''')
c.execute("DROP TABLE IF EXIST gambar")
gambar=open('depresiface.jpg','rb')
gambar2=gambar.read()
gambarbaru=open('gambarbaru.jpg','wb')

gambarsimpen=sqlite3.Binary(gambar2)
c.execute('INSERT INTO gambar VALUES (?)',(gambarsimpen,))
c.execute('SELECT * FROM GAMBAR')
gambarbaru.write(c.fecthone()[0])
c.close()

