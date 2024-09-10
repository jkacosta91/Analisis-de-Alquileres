import requests as rq
import base64
import pandas as pd
import numpy as np
import json
from datetime import date


def get_oauth_token():
    api_key = '1nhlg0vje07ag6jv1ifzzj853gtzbjy7'
    secret = '75RVKDnnE7at'
    
    message = api_key + ":" + secret   # Combine the API key and the secret to get our personalised message

    auth = "Basic " + base64.b64encode(message.encode("ascii")).decode("ascii")   # Encode the message

    headers_dic = {"Authorization" : auth,
                "Content-Type" : "application/x-www-form-urlencoded;charset=UTF-8"}   # Define our headers

    params_dic = {"grant_type" : "client_credentials",   # Define the request params
                "scope" : "read"}

    r = rq.post("https://api.idealista.com/oauth/token",   # Perform the request with the api url, headers and params
                    headers = headers_dic,
                    params = params_dic)

    token = json.loads(r.text)['access_token']   # Obtain the personalised token, as a json

    return token

# This are the params we will use to filter our search

base_url = 'https://api.idealista.com/3.5/es/search'    # Base search url
country = 'es'     # Search country (es, it, pt)                          
language = 'es'     # Search language (es, it, pt, en, ca) 
max_items = '50'     # Max items per call, the maximum set by Idealista is 50
operation = 'sale'     # Kind of operation (sale, rent) 
property_type = 'homes'     # Type of property (homes, offices, premises, garages, bedrooms)
order = ''     # Order of the listings, consult documentation for all the available orders 
center = '41.65606,-0.87734'     # Coordinates of the search center
distance = '4000'     # Max distance from the center
sort = 'desc'     # How to sort the found items
bankOffer = 'false'     # If the owner is a bank
# maxprice = '750'     # Max price of the listings

def define_search_url():
    '''
    This function will combine our params with the url, in order to create our own search url
    '''
    url = (base_url +      
        country +
        '/search?operation=' + operation +
        '&maxItems=' + max_items +
        #'&order=' + order +
        '&center=' + center +
        '&distance=' + distance +
        '&propertyType=' + property_type +
        '&sort=' + sort + 
        '&numPage=%s' +
        #'&maxPrice=' + maxprice +
        '&language=' + language)
    
    return url

url = define_search_url()
url

def search_api(url):  
    '''
    This function will use the token and url created previously, and return our search results.
    '''
    token = get_oauth_token()   #  Get the personalised token

    headers = {'Content-Type': 'Content-Type: multipart/form-data;',   # Define the search headers 
            'Authorization' : 'Bearer ' + token}

    content = rq.post(url, headers = headers)   # Return the content from the request

    result = json.loads(content.text)   # Transform the result as a json file

    return result

# Since we need to give pagination to our search and this is our first search, we will set the pagination as 1
pagination = 1
first_search_url = url %(pagination)

results = search_api(first_search_url)
results

total_pages = results['totalPages']
total_pages

def results_to_df(results):
    df = pd.DataFrame.from_dict(results['elementList'])
    return df

def concat_df(df, df_tot):
    df_tot = pd.concat([df_tot, df])
    return df_tot

df = results_to_df(results)
df_tot = pd.DataFrame()
df_tot = concat_df(df, df_tot)

lugar = 'zaragoza'

for i in range(2, total_pages + 1):
    url_page = url %(i)  # Add the pagination to the copied URL
    results = search_api(url_page)  # Get the search results
    df = results_to_df(results)  # Save the results as a dataframe
    df_tot = concat_df(df, df_tot)  # Concatenate the results to the main dataframe

today = date.today()
file_path = f'idealista_{lugar}_{today}.csv'

def df_to_csv(df):
    df.to_csv(file_path, index=False)  # Save it into a csv

df_to_csv(df_tot)