import mysql.connector
from mysql.connector import errorcode
# connecting to the database using 'connect()' method
# it takes 3 required parameters 'host', 'user', 'passwd'
import config
cnx = mysql.connector .connect(
    host=config.host,
    user=config.user,
    passwd=config.password
)

# create cursor
cursor = cnx.cursor()

## create data base function ##


def create_database(cursor, database):
    try:
        # fucntion to create a db name
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(database))
    # return error message if failing to open a database
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


db_name = 'yelp_project'
# try to create the DB - fail if exists
try:
    cursor.execute("USE {}".format(db_name))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(db_name))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor, db_name)
        print("Database {} created successfully.".format(db_name))
        cnx.database = db_name
    else:
        print(err)
        exit(1)
