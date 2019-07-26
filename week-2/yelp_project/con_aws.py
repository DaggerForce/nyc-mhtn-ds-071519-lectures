# connecting to the database using 'connect()' method
# it takes 3 required parameters 'host', 'user', 'passwd'
import mysql.connector
import config
cnx = mysql.connector .connect(
    host=config.host,
    user=config.user,
    passwd=config.password
)

# create cursor
cursor = cnx.cursor()
