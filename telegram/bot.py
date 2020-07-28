"""
    Модуль предоставляет методы Telegram Bot API
    author: Myshko E.V.
"""

import requests
import configparser
from .telegram_objects import telegram_file
from .telegram_objects import message


class MetaSingleton(type):
    """
        Метакласс синглтона
    """
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class TelegramBot(metaclass=MetaSingleton):
    """
        Класс представляет объект теклеграм бота
    """
    def __init__(self, bot_token=None):
        """
            Инициализация состояния бота
            Params:
                bot_token - токен бота для доступа к Telegram Bot Api
        """
        if bot_token:
            self.bot_token = bot_token
        else:
            config = configparser.ConfigParser()
            config.read('bot.ini')
            self.bot_token = config['Authorization']['Token']
        self.endpoint = f"https://api.telegram.org/bot{self.bot_token}"
        self.file_endpoint = f"https://api.telegram.org/file/bot{self.bot_token}"

    def set_webhook(self, url, allowed_updates=None, certificate=None, max_connections=None):
        """
            Установка webhook для бота
            Params:
                url - HTTPS URL на который будут приходить обновления
                allowed_updates - список типов для которых необходимо получать обновления
                certificate - файл сертификата открытого ключа
                max_connections - максимальное количество подключений к webhook
            Return:
                boolean - успех операции
        """
        params = {"url": url}
        if allowed_updates:
            params["allowed_updates"] = allowed_updates
        if max_connections:
            params["max_connections"] = max_connections
        if certificate:
            params["certificate"] = certificate
        response = requests.get(f"{self.endpoint}/setWebhook", params=params)
        return response.json().get("ok")

    def delete_webhook(self):
        """
            Удаление вебхука
            Return:
                boolean - успех операции
        """
        response = requests.get(f"{self.endpoint}/setWebhook")
        return response.json().get("ok")

    def webhook_info(self):
        """
            Получение информации о состоянии вебхука
            Return:
                dict - информация о состоянии вебхука
        """
        response = requests.get(f"{self.endpoint}/getWebhookInfo")
        return response.json()

    def get_file(self, file_id):
        """
            Получение информации о файле
            Params:
                file_id - идентификатор файла
            Return:
                dict - информация о файле
        """
        response = requests.get(f"{self.endpoint}/getFile", params={"file_id": file_id})
        return response.json()

    def download_file(self, file_id):
        """
            Скачивание файла
            Params:
                file_id - идентификатор файла
            Return:
                bytes - файл
        """
        file_info = self.get_file(file_id)
        api_file = telegram_file.File(file_info["result"])
        if api_file.file_path:
            response = requests.get(f"{self.file_endpoint}/{api_file.file_path}")
            return response.content
        return bytes()

    def send_message(self, chat_id, text, **kwargs):
        """
            Отправка сообщения
            Params:
                chat_id - идентификатор чата в который необходимо отправить сообщение
                text - текст, который необходимо отправить
                kwargs:
                    parse_mode - режим разбора сообщения
                    disable_web_page_preview - отключение предварительного просмотра ссылок
                    disable_notification - отключение уведомления о сообщении
                    reply_to_message_id - идентификатор сообщения на который отправляется ответ
                    reply_markup - дополнительные параметры интерфейса
            Return:
                Message - отправленное сообщение
        """
        params = {"chat_id": chat_id, "text": text}
        if "parse_mode" in kwargs:
            params["parse_mode"] = kwargs["parse_mode"]
        if "disable_web_page_preview" in kwargs:
            params["disable_web_page_preview"] = kwargs["disable_web_page_preview"]
        if "reply_to_message_id" in kwargs:
            params["reply_to_message_id"] = kwargs["reply_to_message_id"]
        if "disable_notification" in kwargs:
            params["disable_notification"] = kwargs["disable_notification"]
        if "reply_markup" in kwargs:
            params["reply_markup"] = kwargs["reply_markup"]
        response = requests.get(f"{self.endpoint}/sendMessage", params=params)
        response_data = response.json()
        if response_data.get("ok"):
            return message.Message(response_data["result"])
        return
