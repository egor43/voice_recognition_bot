"""
    Модуль предоставляет объекты конфигурации распознавания речи
    author: Myshko E.V.
"""

# Перечисление кодировок аудиофайлов
ENCODING_MAP = {"mp3": 12}


class RecognizeConfiguration:
    """
        Конфигурация распознавания речи
    """
    def __init__(self, **kwargs):
        """
            Конструирование конфигурации
            Params:
                kwargs:
                    encoding - кодировка аудиофайла (default="mp3")
                    rate - частота дискретизации
                    num_channels - количество каналов
                    chunk_size - размер частей файла, отправляемых на распознавание (default=1024)
                    max_seconds - максимальное время аудиофайла (default=None)
                    endpoint - конечная точка API распознавания речи (default="stt.tinkoff.ru:443")
                    api_key - ключ API приложения tinkoff voicekit
                    secret_key - секретный ключ tinkoff voicekit
                    ca_file - файл сертификата (default=None)
                    max_alternatives - максимальное количество вариантов распознавания речи (default=1)
                    do_not_perform_vad - обнаружение голосовой активности (default=True)
                    silence_duration_threshold - порог молчания (default=0.6)
                    language_code - язык речи для распознавания (default="ru-RU")
                    disable_automatic_punctuation - автоматическое определение пунктуации (default=False)
        """
        # Обязательные к указанию параметры
        self.rate = kwargs["rate"]
        self.num_channels = kwargs["num_channels"]
        self.api_key = kwargs["api_key"]
        self.secret_key = kwargs["secret_key"]

        # Параметры, имеющие дефолтные значения
        self.encoding = kwargs.get("encoding", ENCODING_MAP.get("mp3"))
        self.chunk_size = kwargs.get("chunk_size", 1024)
        self.max_seconds = kwargs.get("max_seconds")
        self.endpoint = kwargs.get("endpoint", "stt.tinkoff.ru:443")
        self.ca_file = kwargs.get("ca_file")
        self.max_alternatives = kwargs.get("max_alternatives", 1)
        self.do_not_perform_vad = kwargs.get("do_not_perform_vad", True)
        self.silence_duration_threshold = kwargs.get("silence_duration_threshold", 0.6)
        self.language_code = kwargs.get("language_code", "ru-RU")
        self.disable_automatic_punctuation = kwargs.get("disable_automatic_punctuation", False)
