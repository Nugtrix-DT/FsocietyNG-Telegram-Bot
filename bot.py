from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton


def start(update, context):

    button1 = InlineKeyboardButton(
        text='Nugtrix-DT',
        url='https://api.whatsapp.com/send/?phone=593978963202&text&app_absent=0'
    )

    update.message.reply_text(
         text='Hola, Esclavo',
         reply_markup=InlineKeyboardMarkup([
             [button1]
         ])
    )


if __name__ == '__main__':

    updater = Updater(token='YOUR TOKEN', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()
