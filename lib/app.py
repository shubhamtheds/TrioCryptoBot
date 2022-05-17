 #This example uses Python 2.7 and the python-request library.
import os
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import pprint 

url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
parameters = {
  'slug' : 'bitcoin',
  'convert':'INR'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': f"{os.environ['API']}",
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  
  price = data['data']['1']['quote']['INR']['price']
  vol_ch_24h = data['data']['1']['quote']['INR']['volume_change_24h']
  per_ch_30d = data['data']['1']['quote']['INR']['percent_change_30d']
  market_cap = data['data']['1']['quote']['INR']['market_cap']
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)


# df2 = json_normalize(data) 
# print(df2)


