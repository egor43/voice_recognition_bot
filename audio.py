"""
    Модуль предоставляет инструменты представления и преобразования аудиофайлов
    author: Myshko E.V.
"""

import io
import tempfile
from pydub import AudioSegment


class AudioFile:
    """
        Представляет обертку над объектом аудиофайла AudioSegment
    """
    def __init__(self, audio_data, audio_format):
        """
            Конструирование объекта аудиофайла
            Params:
                audio_data - бинарные данные аудиофайла
                audio_format - формат аудиофайла
        """
        if audio_format == "ogg":
            self._original_file = AudioSegment.from_ogg(io.BytesIO(audio_data))
        elif audio_format == "mp3":
            self._original_file = AudioSegment.from_mp3(io.BytesIO(audio_data))
        else:
            raise AttributeError("Неподдерживаемый формат аудиофайла")

    def convert(self, out_format):
        """
            Конвертация аудиофайла в необходимый формат
            Params:
                out_format - формат в который необходимо переконвертировать аудиофайл
            Result:
                AudioFile - сконвертированный аудиофайл
        """
        with tempfile.NamedTemporaryFile() as out_file:
            self._original_file.export(out_file.name, format=out_format)
            result_audio = AudioFile(out_file.read(), out_format)
            return result_audio

    def __getattr__(self, attr):
        """
            Проксирует вызовы атрибутов к внутреннему аудиообъекту
            Params:
                attr - имя атрибута
            Return:
                значение атрибута из внутреннего объекта
        """
        return getattr(self._original_file, attr)
