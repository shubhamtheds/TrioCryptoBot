 #This example uses Python 2.7 and the python-request library.
import os
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start' : '1',
  'limit' : '20',
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
  #BTC DATA
  btc_data_inr = data['data'][0]['quote']['INR']
  
  btc_price = btc_data_inr['price']
  
  btc_vol_ch_24h = btc_data_inr['volume_change_24h']
  
  btc_per_ch_30d = btc_data_inr['percent_change_30d']
  
  btc_market_cap = btc_data_inr['market_cap']


  #ETH DATA
  eth_data_inr = data['data'][1]['quote']['INR']
  eth_price = eth_data_inr['price']
  
  eth_vol_ch_24h = eth_data_inr['volume_change_24h']
  
  eth_per_ch_30d = eth_data_inr ['percent_change_30d']
  
  eth_market_cap = eth_data_inr['market_cap']


  #USDT DATA
  usdt_data_inr = data['data'][2]['quote']['INR']
  usdt_price = usdt_data_inr['price']
  
  usdt_vol_ch_24h = usdt_data_inr['volume_change_24h']
  
  usdt_per_ch_30d = usdt_data_inr ['percent_change_30d']
  
  usdt_market_cap = usdt_data_inr['market_cap']


  #USDC DATA
  usdc_price_inr = data['data'][3]['quote']['INR']
  usdc_price = usdc_price_inr['price']
  
  usdc_vol_ch_24h = usdc_price_inr['volume_change_24h']
  
  usdc_per_ch_30d = usdc_price_inr['percent_change_30d']
  
  usdc_market_cap = usdc_price_inr['market_cap'] 


  #BNB DATA
  bnb_price_inr = data['data'][4]['quote']['INR']
  bnb_price = bnb_price_inr['price']
  
  bnb_vol_ch_24h = bnb_price_inr['volume_change_24h']
  
  bnb_per_ch_30d = bnb_price_inr['percent_change_30d']
  
  bnb_market_cap = bnb_price_inr['market_cap']


  #XRP DATA
  xrp_price_inr = data['data'][5]['quote']['INR']
  xrp_price = xrp_price_inr['price']
  
  xrp_vol_ch_24h = xrp_price_inr['volume_change_24h']
  
  xrp_per_ch_30d = xrp_price_inr ['percent_change_30d']
  
  xrp_market_cap = xrp_price_inr['market_cap']


  #BUSD DATA
  busd_price_inr = data['data'][6]['quote']['INR']
  busd_price = busd_price_inr['price']
  
  busd_vol_ch_24h = busd_price_inr['volume_change_24h']
  
  busd_per_ch_30d = busd_price_inr['percent_change_30d']
  
  busd_market_cap = busd_price_inr['market_cap']  



except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)







