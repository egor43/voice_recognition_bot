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
    def __init__(self, audio_data, audio_format, target_format):
        """
            Конструирование объекта аудиофайла
            Params:
                audio_data - бинарные данные аудиофайла
                audio_format - формат аудиофайла
                target_format - требуемый формат фудиофайла
        """
        self._audio_format = audio_format
        self._target_format = target_format
        if self._audio_format == "ogg":
            self._original_file = AudioSegment.from_ogg(io.BytesIO(audio_data))
        elif self._audio_format == "mp3":
            self._original_file = AudioSegment.from_mp3(io.BytesIO(audio_data))
        else:
            raise AttributeError("Неподдерживаемый формат аудиофайла")

    def read_all(self):
        """
            Чтение всех данных аудиофайла
            Return:
                butes - бинарные данные аудиофайла
        """
        return self.read()

    def read(self, size=-1):
        """
            Чтение аудиофайла в указанном при создании требуемом формате
            Return:
                size=-1 - количество считываемых данных
                butes - бинарные данные аудиофайла
        """
        byte_buffer = io.BytesIO()
        with tempfile.NamedTemporaryFile() as temp_file:
            self._original_file.export(temp_file.name, format=self._target_format)
            byte_buffer.write(temp_file.read(size))
            byte_buffer.seek(0)
        return byte_buffer.read(size)

    def __getattr__(self, attr):
        """
            Проксирует вызовы атрибутов к внутреннему аудиообъекту
            Params:
                attr - имя атрибута
            Return:
                значение атрибута из внутреннего объекта
        """
        return getattr(self._original_file, attr)
