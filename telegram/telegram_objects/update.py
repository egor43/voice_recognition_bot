"""
    Модуль представляет объект Update
    author: Myshko E.V.
"""

from . import message


class Update:
    """
        Объект Telegram Api - Update
    """
    def __init__(self, data: dict):
        """
            Инициализация объекта
            Params: 
                data - данные telegram api, представляющие объект Update
        """
        self.update_id = data["update_id"]
        self.message = message.Message(data["message"]) if "message" in data else None
        self.edited_message = message.Message(data["edited_message"]) if "edited_message" in data else None
        self.channel_post = message.Message(data["channel_post"]) if "channel_post" in data else None
        self.edited_channel_post = message.Message(data["edited_channel_post"]) if "edited_channel_post" in data else None
