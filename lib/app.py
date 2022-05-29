 #This example uses Python 2.7 and the python-request library.
import os
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start' : '1',
  'limit' : '7',
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
  print(data)
  #BTC DATA
  btc_data_inr = data['data'][0]['quote']['INR']
  
  btc_price = btc_data_inr['price']
  
  btc_vol_ch_24h = btc_data_inr['volume_change_24h']
  
  btc_per_ch_30d = btc_data_inr['percent_change_30d']
  
  btc_market_cap = btc_data_inr['market_cap']


  #ETH DATA
  eth_price = data['data'][1]['quote']['INR']['price']
  
  eth_vol_ch_24h = data['data'][1]['quote']['INR']['volume_change_24h']
  
  eth_per_ch_30d = data['data'][1]['quote']['INR'] ['percent_change_30d']
  
  eth_market_cap = data['data'][1]['quote']['INR']['market_cap']


  #USDT DATA
  usdt_price = data['data'][2]['quote']['INR']['price']
  
  usdt_vol_ch_24h = data['data'][2]['quote']['INR']['volume_change_24h']
  
  usdt_per_ch_30d = data['data'][2]['quote']['INR'] ['percent_change_30d']
  
  usdt_market_cap = data['data'][2]['quote']['INR']['market_cap']


  #USDC DATA
  usdc_price = data['data'][3]['quote']['INR']['price']
  
  usdc_vol_ch_24h = data['data'][3]['quote']['INR']['volume_change_24h']
  
  usdc_per_ch_30d = data['data'][3]['quote']['INR'] ['percent_change_30d']
  
  usdc_market_cap = data['data'][3]['quote']['INR']['market_cap'] 


  #BNB DATA
  bnb_price = data['data'][4]['quote']['INR']['price']
  
  bnb_vol_ch_24h = data['data'][4]['quote']['INR']['volume_change_24h']
  
  bnb_per_ch_30d = data['data'][4]['quote']['INR'] ['percent_change_30d']
  
  bnb_market_cap = data['data'][4]['quote']['INR']['market_cap']


  #XRP DATA
  xrp_price = data['data'][5]['quote']['INR']['price']
  
  xrp_vol_ch_24h = data['data'][5]['quote']['INR']['volume_change_24h']
  
  xrp_per_ch_30d = data['data'][5]['quote']['INR'] ['percent_change_30d']
  
  xrp_market_cap = data['data'][5]['quote']['INR']['market_cap']


  #BUSD DATA
  busd_price = data['data'][6]['quote']['INR']['price']
  
  busd_vol_ch_24h = data['data'][6]['quote']['INR']['volume_change_24h']
  
  busd_per_ch_30d = data['data'][6]['quote']['INR'] ['percent_change_30d']
  
  busd_market_cap = data['data'][6]['quote']['INR']['market_cap']  



except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)







