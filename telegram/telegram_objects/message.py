"""
    Модуль представляет объект Update
    author: Myshko E.V.
"""

from . import chat
from . import voice


class Message:
    """
        Объект Telegram Api - Message
    """
    def __init__(self, data: dict):
        """
            Инициализация объекта
            Params:
                data - данные telegram api, представляющие объект Message
        """
        self.message_id = data["message_id"]
        self.date = data["date"]
        self.chat = chat.Chat(data["chat"]) if "chat" in data else None
        self.voice = voice.Voice(data["voice"]) if "voice" in data else None
        self.forward_from_chat = chat.Chat(data["forward_from_chat"]) if "forward_from_chat" in data else None
        self.forward_from_message_id = data.get("forward_from_message_id")
        self.forward_signature = data.get("forward_signature")
        self.forward_sender_name = data.get("forward_sender_name")
        self.forward_date = data.get("forward_date")
        self.reply_to_message = Message(data["reply_to_message"]) if "reply_to_message" in data else None
        self.edit_date = data.get("edit_date")
        self.media_group_id = data.get("media_group_id")
        self.author_signature = data.get("author_signature")
        self.text = data.get("text")
        self.caption = data.get("caption")
        self.new_chat_title = data.get("new_chat_title")
        self.delete_chat_photo = data.get("delete_chat_photo")
        self.group_chat_created = data.get("group_chat_created")
        self.supergroup_chat_created = data.get("supergroup_chat_created")
        self.channel_chat_created = data.get("channel_chat_created")
        self.migrate_to_chat_id = data.get("migrate_to_chat_id")
        self.migrate_from_chat_id = data.get("migrate_from_chat_id")
        self.connected_website = data.get("connected_website")
