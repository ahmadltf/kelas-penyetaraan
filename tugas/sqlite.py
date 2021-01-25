#ahmad luthfi hanif


banyak = [
    ('awla', 'fajri','ayaya@gmail.com')
]
c.execute("INSERT INTO customer VALUES('Mary','Smith','ayaya@gmail.com')")
c.executemany("INSERT INTO customer VALUES (?,?,?)",banyak)

c.execute("SELECT rowid,* FROM customer WHERE email LIKE '%gmail.com' ORDER BY rowid DESC")
c.execute("""UPDATE customer SET first_name = "BOB"
        WHERE last_name="ELDER"
""")
c.execute("""DELETE FROM customer WHERE rowid=6
""")
items= c.fetchall()
for item in items:
