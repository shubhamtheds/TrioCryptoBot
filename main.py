import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from lib.app import *
  

def get_btc_price(update: Update, context: CallbackContext):
    update.message.reply_text(f'₹{btc_price}')

def btc_vol_ch_24h(update: Update, context: CallbackContext):
    update.message.reply_text(f'{btc_vol_ch_24h}%')
  
def btc_per_ch_30d(update: Update, context: CallbackContext):
    update.message.reply_text(f'{btc_per_ch_30d}%')
  
def btc_market_cap(update: Update, context: CallbackContext):
    update.message.reply_text(f'₹{btc_market_cap}')

def eth_price(update: Update, context: CallbackContext):
    update.message.reply_text(f'₹{eth_price}')

def eth_vol_ch_24h(update: Update, context: CallbackContext):
    update.message.reply_text(f'{eth_vol_ch_24h}%')
  
def eth_per_ch_30d(update: Update, context: CallbackContext):
    update.message.reply_text(f'{eth_per_ch_30d}%')
  
def eth_market_cap(update: Update, context: CallbackContext):
    update.message.reply_text(f'₹{eth_market_cap}')

def usdt_price(update: Update, context: CallbackContext):
    update.message.reply_text(f'₹{usdt_price}')

def usdt_vol_ch_24h(update: Update, context: CallbackContext):
    update.message.reply_text(f'{usdt_vol_ch_24h}%')
  
def usdt_per_ch_30d(update: Update, context: CallbackContext):
    update.message.reply_text(f'{usdt_per_ch_30d}%')
  
def usdt_market_cap(update: Update, context: CallbackContext):
    update.message.reply_text(f'₹{usdt_market_cap}')

def usdc_price(update: Update, context: CallbackContext):
    update.message.reply_text(f'₹{usdc_price}')

def usdc_vol_ch_24h(update: Update, context: CallbackContext):
    update.message.reply_text(f'{usdc_vol_ch_24h}%')
  
def usdc_per_ch_30d(update: Update, context: CallbackContext):
    update.message.reply_text(f'{usdc_per_ch_30d}%')
  
def usdc_market_cap(update: Update, context: CallbackContext):
    update.message.reply_text(f'₹{usdc_market_cap}')

def bnb_price(update: Update, context: CallbackContext):
    update.message.reply_text(f'₹{bnb_price}')

def bnb_vol_ch_24h(update: Update, context: CallbackContext):
    update.message.reply_text(f'{bnb_vol_ch_24h}%')
  
def bnb_per_ch_30d(update: Update, context: CallbackContext):
    update.message.reply_text(f'{bnb_per_ch_30d}%')
  
def bnb_market_cap(update: Update, context: CallbackContext):
    update.message.reply_text(f'₹{bnb_market_cap}')

  
updater = Updater(os.environ['TOKEN'])

print("Bot is active! 🚀")


updater.dispatcher.add_handler(CommandHandler('btc_price', get_btc_price))
updater.dispatcher.add_handler(CommandHandler('btc_vol_ch_24h', btc_vol_ch_24h))
updater.dispatcher.add_handler(CommandHandler('btc_per_ch_30d', btc_per_ch_30d))
updater.dispatcher.add_handler(CommandHandler('btc_market_cap', btc_market_cap))

updater.dispatcher.add_handler(CommandHandler('eth_price', eth_price))
updater.dispatcher.add_handler(CommandHandler('eth_vol_ch_24h', eth_vol_ch_24h))
updater.dispatcher.add_handler(CommandHandler('eth_per_ch_30d', eth_per_ch_30d))
updater.dispatcher.add_handler(CommandHandler('eth_market_cap', eth_market_cap))

updater.dispatcher.add_handler(CommandHandler('usdt_price', usdt_price))
updater.dispatcher.add_handler(CommandHandler('usdt_vol_ch_24h', usdt_vol_ch_24h))
updater.dispatcher.add_handler(CommandHandler('usdt_per_ch_30d', usdt_per_ch_30d))
updater.dispatcher.add_handler(CommandHandler('usdt_market_cap', usdt_market_cap))

updater.dispatcher.add_handler(CommandHandler('usdc_price', usdc_price))
updater.dispatcher.add_handler(CommandHandler('usdc_vol_ch_24h', usdc_vol_ch_24h))
updater.dispatcher.add_handler(CommandHandler('usdc_per_ch_30d', usdc_per_ch_30d))
updater.dispatcher.add_handler(CommandHandler('usdc_market_cap', usdc_market_cap))

updater.dispatcher.add_handler(CommandHandler('bnb_price', bnb_price))
updater.dispatcher.add_handler(CommandHandler('bnb_vol_ch_24h', bnb_vol_ch_24h))
updater.dispatcher.add_handler(CommandHandler('bnb_per_ch_30d', bnb_per_ch_30d))
updater.dispatcher.add_handler(CommandHandler('bnb_market_cap', bnb_market_cap))


updater.start_polling()
updater.idle()