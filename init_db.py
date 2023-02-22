import sqlite3

# create a connection to the db
# execute the schema script
connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

# setting a cursor to be able to navigate the rows of the table we create
cursor = connection.cursor()

# cerating dummy content
cursor.execute("INSERT INTO posts (title,content) VALUES (?, ?)",('First post', 'content first post'))
cursor.execute("INSERT INTO posts (title,content) VALUES (?, ?)",('Second post post', 'content second post'))

# commiting the file
connection.commit()
# close the connection
connection.close()

