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
        self.title = get("title")
        self.username = get("username")
        self.first_name = get("first_name")
        self.last_name = get("last_name")
        self.description = get("description")
        self.invite_link = get("invite_link")
        self.pinned_message = message.Message(data["pinned_message"]) if "pinned_message" in data else None
        self.slow_mode_delay = get("slow_mode_delay")
        self.sticker_set_name = get("sticker_set_name")
        self.can_set_sticker_set = get("can_set_sticker_set")

