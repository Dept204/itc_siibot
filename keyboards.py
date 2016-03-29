from telegram import ReplyKeyboardMarkup


class Keyboards:
    def __init__(self):
        self.keyboards = dict()
        self.keyboards['basic'] = [['/start', '/help'], ['/configsii']]

    def get_keyboard(self, key):
        """
        Returns a properly formed Telegram Keyboard
        :param key: Name of the keyboard required
        :return: ReplyKeyboardMarkup
        """
        return ReplyKeyboardMarkup(self.keyboards[key])
