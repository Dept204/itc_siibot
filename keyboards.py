from telegram import ReplyKeyboardMarkup


class Keyboards:
    def __init__(self):
        self.keyboards = dict()
        self.keyboards['basic'] = [['Iniciar', 'Ayuda'], ['Configurar SII']]
        self.keyboards['test'] = [['Uno', 'Dos'], ['Tres', 'Cuatro']]

    def get_keyboard(self, key):
        """
        Returns a properly formed Telegram Keyboard
        :param key: Name of the keyboard required
        :return: ReplyKeyboardMarkup
        """
        return ReplyKeyboardMarkup(self.keyboards[key], resize_keyboard=True)

    def test_handler(self, bot, update):
        bot.sendMessage(update.message.chat_id, reply_markup=self.get_keyboard("test"))
        print update.message.text
