import config
import mysql.connector
import requests
import time
import yelp_config
import json
client_id = yelp_config.my_id
api_key = yelp_config.api


# test run on one busines

def yelp_call(url_params, api_key):
    url = 'GET https://api.yelp.com/v3/businesses/{}/reviews'.format(biz_id)
    headers = {'Authorization': 'Bearer {}'.format(api)}
    response = requests.get(url, headers=headers, params=url_params)

    data = response.json()['businesses']
    return data


locale = 'en_US'
# set reviews paramters
url_params = {'locale': locale,
              }

"""SELECT business_id
FROM business
"""

call_reviews = yelp_call(url_params, api_key)
print(call_reviews)
