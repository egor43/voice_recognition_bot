"""
    Модуль представляет объект Chat
    author: Myshko E.V.
"""


class Chat:
    """
        Объект Telegram Api - Chat
    """
    def __init__(self, data: dict):
        """
            Инициализация объекта
            Params: 
                data - данные telegram api, представляющие объект Chat
        """
        self.id = data["id"]
