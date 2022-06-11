import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from lib.app import *
  
def get_help(update: Update, context: CallbackContext):
    update.message.reply_text("/btc_price, /btc_vol_ch_24h, /btc_per_ch_30d, /btc_market_cap, /eth_price, /eth_vol_ch_24h, /eth_per_ch_30d, /eth_market_cap, /usdt_price, /usdt_vol_ch_24h, /usdt_per_ch_30d, /usdt_market_cap, /usdc_price, /usdc_vol_ch_24h, /usdc_per_ch_30d, /usdc_market_cap, /bnb_price, /bnb_vol_ch_24h, /bnb_per_ch_30d, /bnb_market_cap, /xrp_price, /xrp_vol_ch_24h, /xrp_per_ch_30d, /xrp_market_cap, /busd_price, /busd_vol_ch_24h, /busd_per_ch_30d, /busd_market_cap,/sol_price, /sol_vol_ch_24h, /sol_per_ch_30d, /sol_market_cap")
                              
def get_btc_price(update: Update, context: CallbackContext):
    update.message.reply_text(f'₹{btc_price}')

def get_btc_vol_ch_24h(update: Update, context: CallbackContext):
    update.message.reply_text(f'{btc_vol_ch_24h}%')
  
def get_btc_per_ch_30d(update: Update, context: CallbackContext):
    update.message.reply_text(f'{btc_per_ch_30d}%')
  
def get_btc_market_cap(update: Update, context: CallbackContext):
    update.message.reply_text(f'₹{btc_market_cap}')

def get_eth_price(update: Update, context: CallbackContext):
    update.message.reply_text(f'₹{eth_price}')

def get_eth_vol_ch_24h(update: Update, context: CallbackContext):
    update.message.reply_text(f'{eth_vol_ch_24h}%')
  
def get_eth_per_ch_30d(update: Update, context: CallbackContext):
    update.message.reply_text(f'{eth_per_ch_30d}%')
  
def get_eth_market_cap(update: Update, context: CallbackContext):
    update.message.reply_text(f'₹{eth_market_cap}')

def get_usdt_price(update: Update, context: CallbackContext):
    update.message.reply_text(f'₹{usdt_price}')

def get_usdt_vol_ch_24h(update: Update, context: CallbackContext):
    update.message.reply_text(f'{usdt_vol_ch_24h}%')
  
def get_usdt_per_ch_30d(update: Update, context: CallbackContext):
    update.message.reply_text(f'{usdt_per_ch_30d}%')
  
def get_usdt_market_cap(update: Update, context: CallbackContext):
    update.message.reply_text(f'₹{usdt_market_cap}')

def get_usdc_price(update: Update, context: CallbackContext):
    update.message.reply_text(f'₹{usdc_price}')

def get_usdc_vol_ch_24h(update: Update, context: CallbackContext):
    update.message.reply_text(f'{usdc_vol_ch_24h}%')
  
def get_usdc_per_ch_30d(update: Update, context: CallbackContext):
    update.message.reply_text(f'{usdc_per_ch_30d}%')
  
def get_usdc_market_cap(update: Update, context: CallbackContext):
    update.message.reply_text(f'₹{usdc_market_cap}')

def get_bnb_price(update: Update, context: CallbackContext):
    update.message.reply_text(f'₹{bnb_price}')

def get_bnb_vol_ch_24h(update: Update, context: CallbackContext):
    update.message.reply_text(f'{bnb_vol_ch_24h}%')
  
def get_bnb_per_ch_30d(update: Update, context: CallbackContext):
    update.message.reply_text(f'{bnb_per_ch_30d}%')
  
def get_bnb_market_cap(update: Update, context: CallbackContext):
    update.message.reply_text(f'₹{bnb_market_cap}')

def get_xrp_price(update: Update, context: CallbackContext):
    update.message.reply_text(f'₹{btc_price}')

def get_xrp_vol_ch_24h(update: Update, context: CallbackContext):
    update.message.reply_text(f'{btc_vol_ch_24h}%')
  
def get_xrp_per_ch_30d(update: Update, context: CallbackContext):
    update.message.reply_text(f'{btc_per_ch_30d}%')
  
def get_xrp_market_cap(update: Update, context: CallbackContext):
    update.message.reply_text(f'₹{btc_market_cap}')

def get_busd_price(update: Update, context: CallbackContext):
    update.message.reply_text(f'₹{busd_price}')

def get_busd_vol_ch_24h(update: Update, context: CallbackContext):
    update.message.reply_text(f'{busd_vol_ch_24h}%')
  
def get_busd_per_ch_30d(update: Update, context: CallbackContext):
    update.message.reply_text(f'{busd_per_ch_30d}%')
  
def get_busd_market_cap(update: Update, context: CallbackContext):
    update.message.reply_text(f'₹{busd_market_cap}')

def get_sol_price(update: Update, context: CallbackContext):
    update.message.reply_text(f'₹{sol_price}')

def get_sol_vol_ch_24h(update: Update, context: CallbackContext):
    update.message.reply_text(f'{sol_vol_ch_24h}%')
  
def get_sol_per_ch_30d(update: Update, context: CallbackContext):
    update.message.reply_text(f'{sol_per_ch_30d}%')
  
def get_sol_market_cap(update: Update, context: CallbackContext):
    update.message.reply_text(f'₹{sol_market_cap}')



  
updater = Updater(os.environ['TOKEN'])

print("Bot is active! 🚀")


updater.dispatcher.add_handler(CommandHandler('btc_price', get_btc_price))
updater.dispatcher.add_handler(CommandHandler('btc_vol_ch_24h', get_btc_vol_ch_24h))
updater.dispatcher.add_handler(CommandHandler('btc_per_ch_30d', get_btc_per_ch_30d))
updater.dispatcher.add_handler(CommandHandler('btc_market_cap', get_btc_market_cap))

updater.dispatcher.add_handler(CommandHandler('eth_price', get_eth_price))
updater.dispatcher.add_handler(CommandHandler('eth_vol_ch_24h', get_eth_vol_ch_24h))
updater.dispatcher.add_handler(CommandHandler('eth_per_ch_30d', get_eth_per_ch_30d))
updater.dispatcher.add_handler(CommandHandler('eth_market_cap', get_eth_market_cap))

updater.dispatcher.add_handler(CommandHandler('usdt_price', get_usdt_price))
updater.dispatcher.add_handler(CommandHandler('usdt_vol_ch_24h', get_usdt_vol_ch_24h))
updater.dispatcher.add_handler(CommandHandler('usdt_per_ch_30d', get_usdt_per_ch_30d))
updater.dispatcher.add_handler(CommandHandler('usdt_market_cap', get_usdt_market_cap))

updater.dispatcher.add_handler(CommandHandler('usdc_price', get_usdc_price))
updater.dispatcher.add_handler(CommandHandler('usdc_vol_ch_24h', get_usdc_vol_ch_24h))
updater.dispatcher.add_handler(CommandHandler('usdc_per_ch_30d', get_usdc_per_ch_30d))
updater.dispatcher.add_handler(CommandHandler('usdc_market_cap', get_usdc_market_cap))

updater.dispatcher.add_handler(CommandHandler('bnb_price', get_bnb_price))
updater.dispatcher.add_handler(CommandHandler('bnb_vol_ch_24h', get_bnb_vol_ch_24h))
updater.dispatcher.add_handler(CommandHandler('bnb_per_ch_30d', get_bnb_per_ch_30d))
updater.dispatcher.add_handler(CommandHandler('bnb_market_cap', get_bnb_market_cap))

updater.dispatcher.add_handler(CommandHandler('xrp_price', get_xrp_price))
updater.dispatcher.add_handler(CommandHandler('xrp_vol_ch_24h', get_xrp_vol_ch_24h))
updater.dispatcher.add_handler(CommandHandler('xrp_per_ch_30d', get_xrp_per_ch_30d))
updater.dispatcher.add_handler(CommandHandler('xrp_market_cap', get_xrp_market_cap))

updater.dispatcher.add_handler(CommandHandler('busd_price', get_busd_price))
updater.dispatcher.add_handler(CommandHandler('busd_vol_ch_24h', get_busd_vol_ch_24h))
updater.dispatcher.add_handler(CommandHandler('busd_per_ch_30d', get_busd_per_ch_30d))
updater.dispatcher.add_handler(CommandHandler('busd_market_cap', get_busd_market_cap))

updater.dispatcher.add_handler(CommandHandler('sol_price', get_sol_price))
updater.dispatcher.add_handler(CommandHandler('sol_vol_ch_24h', get_sol_vol_ch_24h))
updater.dispatcher.add_handler(CommandHandler('sol_per_ch_30d', get_sol_per_ch_30d))
updater.dispatcher.add_handler(CommandHandler('sol_market_cap', get_sol_market_cap))

updater.dispatcher.add_handler(CommandHandler('help', get_help))

updater.start_polling()
updater.idle()