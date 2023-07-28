import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()

# cur.execute('drop table users')
# connection.commit()


with open('schema.sql') as f:
    connection.executescript(f.read())


cur.execute('insert into users (email, username, password, admin) values (?, ?, ?, ?)',
            ('admin@example.com', 'admin', 'password', True)
            )

connection.commit()
connection.close()
