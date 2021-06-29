from telegram.ext import Updater, CommandHandler


def start(update, context):

    update.message.reply_text('Hola, Esclavo')


if __name__ == '__main__':

    updater = Updater(token='1823188219:AAGrfAdDAFvr38COWGThFFnx2CJv2nrYZPo', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()
