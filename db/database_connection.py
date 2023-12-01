from psycopg2 import connect

from settings.settings import DATABASE

# Connect to an existing database
db_connection = connect(**DATABASE)

# Open a cursor to perform database operations
db = db_connection.cursor()

