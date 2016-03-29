# coding=utf-8
from telegram.ext import Updater
from telegram import ReplyKeyboardMarkup
import os
from user import User
# For call
siitag = '/configsii '


def start(bot, update):
    bot.sendMessage(update.message.chat_id, text="Bot para el SII (No Oficial) del ITC")


def help(bot, update):
    reply_markup = ReplyKeyboardMarkup([['/start', '/help'],
                                            ['/configsii']])
    bot.sendMessage(update.message.chat_id, text='Ayuda', reply_markup = reply_markup)


def handler(bot, update):
    if 'sii' in update.message.text:
        tmpuser = User(update.message.chat_id)
        send_message(bot, update, tmpuser.command(update.message.text.replace('sii ', '')))
    else:
        send_message(bot, update,'Para una lista completa de ayuda, escriba <b>help</b>, para ayuda específica sobre un comando, escriba <b>help comando</b>')


def config_sii(bot, update):
    try:
        data = update.message.text.replace(siitag, '').split()
        u = User(update.message.chat_id)
        if data[0] == 'update':
            data = data[1:]
            result = u.update_data(data)
        elif data[0] == 'set':
            data = data[1:]
            result = u.register(data)
        elif data[0] == 'delete':
            result = u.delete()
        else:
            result = 'Comando no reconocido'
        send_message(bot, update, result)
    except StandardError:
        send_message(bot, update, 'Ocurrió un error, revise su comando')


def send_message(bot, update, message):
    bot.sendMessage(update.message.chat_id, text=message, parse_mode='HTML')
    return True


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(os.environ['TELEGRAM_BOT_API_KEY'])

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.addTelegramCommandHandler("start", start)
    dp.addTelegramCommandHandler("help", help)
    dp.addTelegramCommandHandler("configsii", config_sii)

    # on noncommand i.e message - echo the message on Telegram
    # dp.addTelegramInlineHandler(inlinequery)

    dp.addTelegramMessageHandler(handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
