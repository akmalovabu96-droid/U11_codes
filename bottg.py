from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

TOKEN = "8047728624:AAFOzFmIwIZPz1pw1BK5hIBLZyRedWDqm2c"


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Salom! Men sizning Telegram botingizman.")


def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)


updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))


updater.start_polling()
updater.idle()

