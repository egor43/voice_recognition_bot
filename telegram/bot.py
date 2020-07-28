"""
    Модуль предоставляет методы Telegram Bot API
    author: Myshko E.V.
"""

import requests


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
    def __init__(self, bot_token):
        """
            Инициализация состояния бота
            Params:
                bot_token - токен бота для доступа к Telegram Bot Api
        """
        self.bot_token = bot_token
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
