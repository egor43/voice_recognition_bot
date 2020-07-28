"""
    Модуль представляет объект File
    author: Myshko E.V.
"""


class File:
    """
        Объект Telegram Api - File
    """
    def __init__(self, data: dict):
        """
            Инициализация объекта
            Params:
                data - данные telegram api, представляющие объект File
        """
        self.file_id = data["file_id"]
        self.file_unique_id = data["file_unique_id"]
        self.file_path = data.get("file_path")
        self.file_size = data.get("file_size")
