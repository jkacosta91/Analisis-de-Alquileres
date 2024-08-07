import requests
import base64
import pandas as pd
import numpy as np
import json

# First we need the client secret and api key

apikey = '1nhlg0vje07ag6jv1ifzzj853gtzbjy7'
client_secret = '75RVKDnnE7at'

# above you replace for the Api Key and client code you received

# Concatenating the credentials into one variable(string)

credentials = f"{apikey}:{client_secret}"

# After we need to encode the api key and client secret
encoded_credentials = base64.b64encode(credentials.encode()).decode()

# url which we will request the token

token_url = "https://api.idealista.com/oauth/token"

# determine the data

data = {"grant_type": "client_credentials",
        "scope": "read"}

# headers

headers = {"Authorization": f"Basic {encoded_credentials}", "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}

# getting response

response = requests.post(token_url, data=data, headers=headers)

# checking status

if response.status_code == 200:
    # Parse the JSON response
    token_data = response.json()

    # Access token received
    c = token_data["access_token"]

    # Print access token and other details
    print("Access Token:", token_data)
    print("Token Type:", token_data["token_type"])
    print("Expires In (seconds):", token_data["expires_in"])
    print("Scope:", token_data["scope"])
else:
    print("Error:", response.status_code, response.text)

# Storing the access token in a variable

access_token = token_data["access_token"]

# Detailing the parameters

base_url = 'https://api.idealista.com/3.5/'  # Base search url
country = 'es'     # Search country (es, it, pt)
language = 'es'     # Search language (es, it, pt, en, ca)
max_items = '50'     # Max items per call, the maximum set by Idealista is 50
operation = 'rent'     # Kind of operation (sale, rent)
property_type = 'homes'     # Type of property (homes, offices, premises, garages, bedrooms)
order = 'priceDown'     # Order of the listings, consult documentation for all the available orders
center = '41.3851,2.1734'     # Coordinates of the search center
distance = '90000'     # Max distance from the center
sort = 'desc'     # How to sort the found items
maxprice = '100000'     # Max price of the listings

# Creating the URL with the parameteres I want 

def define_search_url():
    url = (base_url +
            country +
            '/search?operation=' + operation +
            '&maxItems=' + max_items +
            '&order=' + order +
            '&center=' + center +
            '&distance=' + distance +
            '&propertyType=' + property_type +
            '&sort=' + sort +
            '&numPage=%s' +
            '&maxPrice=' + maxprice +
            '&language=' + language)
    return url

url = define_search_url()
url

def search_api(url):
    token = access_token  # Get the personalized token

    headers = {'Content-Type': "application/json",
                'Authorization': 'Bearer ' + token}

    content = requests.post(url, headers=headers)

    if content.status_code == 200:
        results = json.loads(content.text)
        return results
    else:
        print(f"API error: {content.status_code}, {content.text}")
        return {}

pagination = 1
first_search_url = url %(pagination)
results = search_api(first_search_url)
if results:
    total_pages = results['totalPages']
else:
    print("Empty response or API error. Setting total_pages to 0.")
    total_pages = 0
total_pages = results['totalPages']

def results_to_df(results):
    if results:  # Check if results is not None
        df = pd.DataFrame.from_dict(results['elementList'])
        return df
    else:
        return pd.DataFrame()

def concat_df(df, df_tot):
    df_tot = pd.concat([df_tot, df])
    return df_tot

df = results_to_df(results)
df_tot = pd.DataFrame()
df_tot = concat_df(df, df_tot)

for i in range(1, total_pages + 1):
    url_copy = url  # Make a copy of the original URL
    url_copy = url_copy % (i)  # Add the pagination to the copied URL
    results = search_api(url_copy)  # Get the search results
    df = results_to_df(results)  # Save the results as a dataframe
    df_tot = concat_df(df, df_tot)  # Concatenate the results to the main dataframe

file_path = 'idealista.csv'

def df_to_csv(df):
    df = df.reset_index()  # Reset the index in order to organize the records
    df.to_csv(file_path, index=False)  # Save it into a csv

df_to_csv(df_tot)

# final dataset:

df_tot