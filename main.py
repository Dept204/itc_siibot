# coding=utf-8
from telegram.ext import Updater
from keyboards import Keyboards
from telegram import ForceReply
from user import User
from redis_handler import Redis
import os

# For call
siitag = '/configsii '
# Keyboards
k = Keyboards()
# Redis db handler
db = Redis()


def start(bot, update):
    bot.sendMessage(update.message.chat_id, text="Bot para el SII (No Oficial) del ITC")
    db.r_message.set(update.message.chat_id, '/start', 3600, nx=True)


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Ayuda', reply_markup=k.get_keyboard("basic"))


def handler(bot, update):
    db.r_message.set(update.message.chat_id, update.message.text)
    tmpuser = User(update.message.chat_id)
    if 'sii' in update.message.text:
        send_message(bot, update, tmpuser.command(update.message.text.replace('sii ', '')))
    elif 'Datos de acceso' == update.message.text:
        show_keyboard(bot, update, k.get_keyboard('config_a'), '¿Qué desea hacer?')
    elif 'Definir' == update.message.text:
        if tmpuser.register_status:
            send_message(bot, update, 'Usted ya tiene datos definidos.')
        else:
            send_message_force(bot, update, 'Ingrese su usuario <i>ej: 12345678</i>')
    elif 'Modificar' == update.message.text:
        pass
    elif 'Eliminar' == update.message.text:
        pass
    else:
        send_message(bot, update,
                     "Para una lista completa de ayuda, escriba <b>help</b>, para ayuda específica sobre un comando, escriba <b>help comando</b>")
    db.r_message.set(update.message.chat_id, '/start', 3600, xx=True)


def config(bot, update):
    if update.message.text == 'Datos de acceso':
        show_keyboard(bot, update, k.get_keyboard('config_a'), '¿Qué desea hacer?')
    else:
        show_keyboard(bot, update, k.get_keyboard('config'))


def last_message(bot, update):
    print db.r_message.get(update.message.chat_id)
    send_message(bot, update, db.r_message.get(update.message.chat_id))


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


def send_message_force(bot, update, message):
    bot.sendMessage(update.message.chat_id, text=message, parse_mode='HTML', force_reply=ForceReply(force_reply=True))


def show_keyboard(bot, update, keyboard, text='Elija una opción'):
    bot.sendMessage(update.message.chat_id, text=text, reply_markup=keyboard)


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(os.environ['TELEGRAM_BOT_API_KEY'])

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.addTelegramCommandHandler("start", start)
    dp.addTelegramCommandHandler("help", help)
    dp.addTelegramCommandHandler("configsii", config_sii)
    dp.addTelegramCommandHandler("config", config)
    dp.addTelegramCommandHandler("last_message", last_message)

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
