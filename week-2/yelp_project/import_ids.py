import config
import mysql.connector
import yelp_config
import requests
import re
import json

# create connection to flatiron database and fetch all the ids for the reviews
cnx = mysql.connector.connect(
    host=config.host, user=config.user, passwd=config.password, database=config.DB_NAME)
cursor = cnx.cursor()
query = ("Select business_id from business")
cursor.execute(query)

# save the query on a new variable
for business_id in cursor:
    business_ids.append(business_id[0])

cursor.close()
cnx.close()


# set reviews paramters
locale = 'en_US'
url_params = {'locale': locale}

# get one review


def get_one_review(biz_id):
    url = "https://api.yelp.com/v3/businesses/{}/reviews".format(biz_id)
    headers = {'Authorization': 'Bearer {}'.format(yelp_config.api)}
    response = requests.get(url, headers=headers, params=url_params)
    data = response.json()['reviews']
    return data


# review = get_one_review(business_ids[0])
# print(type(review))
# print(len(review))
# print(review[0]['time_created'])
# print(business_ids[0])


def get_all_reviews(b_ids):
    reviews = []
    for b_id in b_ids:
        try:
            reviews.append(get_one_review(b_id))
        except:
            print(f'failed to get the review for {b_id}')
    return reviews


def create_data_structure(b_ids):
    counter = 0
    try:
        for k, v in business_dict.items():
            if k == 'id':
                data_dict['review_id'] = v
            elif k == 'time_created':
                data_dict[k] = v

        return data_dict

    # reviews = []
    # review_dict = {}
    # counter = 0
    # for an_id in b_ids:
    #     try:
    #         review = get_one_review(an_id[i])
    #         review_dict['review_id'] = review['id']
    #         review_dict['time_created'] = review['time_created']
    #         review_dict['business_id'] = b_ids[counter]
    #         reviews.append(review_dict)
    #         counter += 1
    #     except:
    #         print(f'failed to get the review for {an_id}')
    #         counter += 1
    # return reviews


reviews = create_data_structure(business_ids)
print(len(reviews))


# IN A PERFECT WORLD WE WOULD IMPORT THESE FUNCTIONS FROM OUR OTHER LOCATION
###################################################################################################
# query for data insertion

# re-arange the data for a single busines


def create_datum(dict_datum):
    try:
        datum = (dict_datum['review_id'], dict_datum['time_created'],
                 dict_datum['business_id'])

    except:
        pass
    return datum


def create_data(business_data):
    data = []
    for biz_dict in business_data:
        data.append(create_datum(biz_dict))
    return data


# parse the data we need


def db_insertion(query, data):
    for datum in data:
        try:
            cursor.execute(query, datum)
            cnx.commit()

        except:
            continue
    print('insert worked')
    pass


add_review = ("INSERT INTO business "
              "(review_id, time_created, business_id) "
              "VALUES (%s, %s, %s)")
db_insertion(add_review, reviews)
# insert the business data ito db

# Make sure data is committed to the database
cnx.commit()
# make sure the connection is closed.
cursor.close()
cnx.close()
#########################################################################################################
