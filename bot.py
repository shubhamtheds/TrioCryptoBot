import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hello(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater(os.environ['TOKEN'])

print("Bot is active! 🚀")

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()