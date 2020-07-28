"""
    Модуль представляет объект Chat
    author: Myshko E.V.
"""

from . import message


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
        self.type = data["type"]
        self.title = data.get("title")
        self.username = data.get("username")
        self.first_name = data.get("first_name")
        self.last_name = data.get("last_name")
        self.description = data.get("description")
        self.invite_link = data.get("invite_link")
        self.pinned_message = message.Message(data["pinned_message"]) if "pinned_message" in data else None
        self.slow_mode_delay = data.get("slow_mode_delay")
        self.sticker_set_name = data.get("sticker_set_name")
        self.can_set_sticker_set = data.get("can_set_sticker_set")
