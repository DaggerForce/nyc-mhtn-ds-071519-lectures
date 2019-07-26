import mysql.connector
from mysql.connector import errorcode
# # connecting to the database using 'connect()' method
# # it takes 3 required parameters 'host', 'user', 'passwd'
import config
cnx = mysql.connector .connect(
    host=config.host,
    user=config.user,
    passwd=config.password
)

# # create cursor
cursor = cnx.cursor()

# ## create data base function ##


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

# creating the queries for the actual tables setting business id as a primary key and a foreign key
DB_NAME = 'yelp_project'
TABLES = {}
TABLES['business'] = (
    "CREATE TABLE business ("
    "  business_id varchar(24) NOT NULL,"
    "  business_name varchar(128) NOT NULL,"
    "  rating float(6) NOT NULL,"
    "  price varchar(10),"
    "  PRIMARY KEY (business_id)"
    ") ENGINE=InnoDB")

TABLES['reviews'] = (
    "CREATE TABLE reviews ("
    "  review_id varchar(128) NOT NULL,"
    "  time_created varchar(24) NOT NULL,"
    "  business_id varchar(128) NOT NULL,"
    "  PRIMARY KEY (review_id),  "
    "  CONSTRAINT c1 "
    "  FOREIGN KEY fk_business_id(business_id)"
    "  REFERENCES business(business_id) ON DELETE CASCADE"
    ") ENGINE=InnoDB")


# create the table using
cnx = mysql.connector.connect(
    host=config.host, user=config.user, passwd=config.password, database=DB_NAME)
cursor = cnx.cursor()

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()
