import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from lib.app import price, vol_ch_24h, per_ch_30d, market_cap


def hello(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def btc_price(update: Update, context: CallbackContext):
    update.message.reply_text(f'₹{price}')

def btc_vol_ch_24h(update: Update, context: CallbackContext):
    update.message.reply_text(f'{vol_ch_24h}')
  
def btc_per_ch_30d(update: Update, context: CallbackContext):
    update.message.reply_text(f'{per_ch_30d}')
  
def btc_market_cap(update: Update, context: CallbackContext):
    update.message.reply_text(f'₹{market_cap}')
  
updater = Updater(os.environ['TOKEN'])

print("Bot is active! 🚀")

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('btc_price', btc_price))
updater.dispatcher.add_handler(CommandHandler('btc_vol_ch_24h', btc_vol_ch_24h))
updater.dispatcher.add_handler(CommandHandler('btc_per_ch_30d', btc_per_ch_30d))
updater.dispatcher.add_handler(CommandHandler('btc_market_cap', btc_market_cap))


updater.start_polling()
updater.idle()