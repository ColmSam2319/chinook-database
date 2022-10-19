import psycopg2


# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the "artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "Name" column from the "artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only the "Queen"  from the "artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 3 - select only the "Queen"  from the "artist" table
cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', ["51"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)
