from datetime import date, datetime, timedelta
import config
import mysql.connector
import json


DB_NAME = 'yelp_project'
# connecting my db and start inserting data into it
cnx = mysql.connector.connect(
    host=config.host,
    user=config.user,
    passwd=config.password,
    database=DB_NAME
)
cursor = cnx.cursor()
# create business query
add_business = ("INSERT INTO business "
                "(business_id, business_name, rating, price) "
                "VALUES (%s, %s, %s, %s)")

# re-arange the data for a single business


def create_datum(dict_datum):
    datum = (dict_datum['id'], dict_datum['name'],
             dict_datum['rating'], dict_datum['price'])
    return datum


add_data = create_datum(business_data)

# insert the business data ito db
cursor.execute(add_business, add_data)
business_id = cursor.lastrowid

# Make sure data is committed to the database
cnx.commit()
# make sure the connection is closed.
cursor.close()
cnx.close()
