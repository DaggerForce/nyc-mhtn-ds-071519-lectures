import config
import mysql.connector
import requests
import time
import yelp_config
import json

# retrieve my yelp credidentials
client_id = yelp_config.my_id
api_key = yelp_config.api

# ping yelp API and retrive the business search


def yelp_call(url_params, api_key):
    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': 'Bearer {}'.format(api_key)}
    response = requests.get(url, headers=headers, params=url_params)

    data = response.json()['businesses']
    return data


def all_results(url_params, api_key):
    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': 'Bearer {}'.format(api_key)}
    response = requests.get(url, headers=headers, params=url_params)
    num = response.json()['total']
    print('{} total matches found.'.format(num))
    cur = 0
    results = []
    while cur < num and cur < 1000:
        url_params['offset'] = cur
        results.append(yelp_call(url_params, api_key))
        time.sleep(1)  # Wait a second
        cur += 50
    print('all_results worked')
    return results


term = 'burgers'
location = 'Brooklyn NY'
url_params = {'term': term.replace(' ', '+'),
              'location': location.replace(' ', '+'),
              'limit': 50
              }
#
raw_business_data = all_results(url_params, api_key)
#

def get_reviews(biz_id):
    url = "https://api.yelp.com/v3/businesses/{}/reviews".format(biz_id)
    headers = {'Authorization': 'Bearer {}'.format(yelp_config.api)}
    response = requests.get(url, headers=headers, params=url_params)
    data = response.json()['reviews']
    return data

def get_all_reviews(b_ids):
    reviews = []
    for b_id in b_ids:
        try:
            reviews.append(get_one_review(b_id))
        except:
            print(f'failed to get the review for {b_id}')
    return reviews


#skiming business data 
#################################################
def datum_dict(business_dict):
    ''' this function receives a dictionary with all the yelp keys and returns
        a new dictionary with only the name, id, rating and price. and a dictionary with only the business keys'''
    data_dict = {}
    for k, v in business_dict.items():
        if k == 'id':
            data_dict[k] = v
        elif k == 'name':
            data_dict[k] = v
        elif k == 'rating':
            data_dict[k] = v
        elif k == 'price':
            data_dict[k] = v
    return data_dict


#skimming reviews
#################################################


# repeat the skimming proccess for all our data giving us a list of dictionaries
def get_dict_from_data(dict_list):
    '''this function returns a a dictionary from a list of dictionary'''
    business_list = []
    for a_list in dict_list:
        for business in a_list:
            try:
                business_list.append(datum_dict(business))
            except:
                continue
    print('get_dict worked')
    return 

# get list of all the businesses dictionary's
skim_business_data = get_dict_from_data(raw_business_data)
################################################################################3




#### skim_data_for1 = get_dict_from_data(raw_data_for_page)
# create business query, add the data and commit query
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
    try:
        datum = (dict_datum['id'], dict_datum['name'],
                 dict_datum['rating'], dict_datum['price'])

    except:
        datum = (dict_datum['id'], dict_datum['name'],
                 dict_datum['rating'], 'NULL')
    print('create_datum worked')
    return datum


def create_data(business_data):
    data = []
    for biz_dict in business_data:
        data.append(create_datum(biz_dict))
    return data


# parse the data we need
data_for_db = create_data(skim_business_data)
#####data_for_db = create_data(skim_data_for1)


def db_insertion(query, data):
    broken = []
    for datum in data:
        try:
            cursor.execute(query, datum)
            cnx.commit()

        except:
            broken.append(datum)
            continue
    pass


# insert the business data ito db
db_insertion(add_business, data_for_db)

# Make sure data is committed to the database
cnx.commit()
# make sure the connection is closed.
cursor.close()
cnx.close()
