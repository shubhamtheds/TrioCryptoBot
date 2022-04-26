from selenium import webdriver
import time, datetime, telegram_send
from telegram import *
from telegram.ext import *
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# driver = webdriver.Chrome()
options = Options()
options.binary_location = "C:\Program Files\Google\Chrome Dev\Application\chrome.exe"
driver = webdriver.Chrome(chrome_options = options, executable_path=r'C:\Program Files\Google\Chrome Dev\Application\chromedriver.exe')
driver.get("https://coinmarketcap.com/")

bot = Bot("5389451244:AAHv5H5j1ug3Cee00dsMVD10O4dD4BoE4Ik")
# print(bot.get_me())

updater = Updater("5389451244:AAHv5H5j1ug3Cee00dsMVD10O4dD4BoE4Ik", use_context=True)

dispatcher = updater.dispatcher

def btc_name(update:Update, context:CallbackContext):
    btcname = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div/div[5]/table/tbody/tr[1]/td[3]/div/a/div/div/p').text
    
    bot.send_message(
        chat_id=update.effective_chat.id,
        text=btcname
    )

def btc_price(update:Update, context:CallbackContext):
    btcprice = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div/div[5]/table/tbody/tr[1]/td[4]/div/a/span').text
    
    bot.send_message(
        chat_id=update.effective_chat.id,
        text=btcprice
    )

def btc_24h(update:Update, context:CallbackContext):
    change = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div/div[5]/table/tbody/tr[1]/td[5]/span').text
    
    bot.send_message(
        chat_id=update.effective_chat.id,
        text=change
    )

def btc_message(update:Update, context:CallbackContext):
    message = {'btc full name': '/btc',
        'btc price': '/btc_price',
        'btc 24 hour change': '/btc_24h'}
    
    bot.send_message(
        chat_id=update.effective_chat.id,
        text=str(message)
    )



start_value=CommandHandler('btc', btc_name)
price_value=CommandHandler('btc_price', btc_price)
change_value=CommandHandler('btc_24h', btc_24h)
message_value=CommandHandler('help', btc_message)


dispatcher.add_handler(start_value)
dispatcher.add_handler(price_value)
dispatcher.add_handler(change_value)
dispatcher.add_handler(message_value)


updater.start_polling()







