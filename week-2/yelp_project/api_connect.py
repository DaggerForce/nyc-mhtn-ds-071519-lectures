# Your code here; use a function or loop to retrieve all the results from your original request
import requests
import time
import yelp_config
import json

client_id = yelp_config.my_id
api_key = yelp_config.api


def yelp_call(url_params, api_key):
    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': 'Bearer {}'.format(api_key)}
    response = requests.get(url, headers=headers, params=url_params)

    data = response.json()['businesses']
    return data


# def all_results(url_params, api_key):
#     num = response.json()['total']
#     print('{} total matches found.'.format(num))
#     cur = 0
#     results = []
#     while cur < num and cur < 1000:
#         url_params['offset'] = cur
#         results.append(yelp_call(url_params, api_key))
#         time.sleep(1)  # Wait a second
#         cur += 50
#     return results


term = 'burgers'
location = 'Brooklyn NY'
url_params = {'term': term.replace(' ', '+'),
              'location': location.replace(' ', '+'),
              'limit': 50
              }


#test123 = yelp_call(url_params, api_key)
# df = all_results(url_params, api_key)
# print(len(df))
# df.head()
