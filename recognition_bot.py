"""
    Реализация простейшего телеграмм бота распознавания речи
"""
import requests
import audio
import os
from flask import Flask
from flask import request
from telegram import bot
from telegram.telegram_objects import update
from recognize import recognize

app = Flask(__name__)

@app.route(f"/", methods=["POST"])
def main_worker():
    """
        Основной воркер - обработчик обновлений
    """
    try:
        update_data = request.get_json()
        update_obj = update.Update(update_data)
        if update_obj.message.voice:
            voice_file = bot.download_file(update_obj.message.voice.file_id)
            if not voice_file:
                return "ok"
            audio_file = audio.AudioFile(voice_file, "ogg", "mp3")
            voice_text = recognize(audio_file)
            bot.send_message(update_obj.message.chat.id, voice_text, reply_to_message_id=update_obj.message.message_id)
    # В любом случае отдаем "ok" чтобы повторно не получать обновление
    except Exception as exc:
        return "ok"
    return "ok"


bot = bot.TelegramBot()
bot.set_webhook(os.environ["BOT_HOST_ADDRESS"], ["message"], max_connections=1)

app.run(host="localhost", port=2004)
