"""
    Модуль представляет объект Voice
    author: Myshko E.V.
"""


class Voice:
    """
        Объект Telegram Api - Voice
    """
    def __init__(self, data: dict):
        """
            Инициализация объекта
            Params: 
                data - данные telegram api, представляющие объект Voice
        """
        self.file_id = data["file_id"]
        self.file_unique_id = data["file_unique_id"]
        self.duration = data["duration"]
        self.mime_type = data.get("mime_type")
        self.file_size = data.get("file_size")
