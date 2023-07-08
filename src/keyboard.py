from src.item import Item


class Mixin:
    def __init__(self):
        self.__language = 'EN'

    def change_lang(self):
        if self.language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self

    @property
    def language(self):
        return self.__language


class Keyboard(Item, Mixin):
    pass
