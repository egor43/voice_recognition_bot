"""
    Модуль предоставляет доступ к инструментам распознавания голоса
    author: Myshko E.V.
"""
import requests
import configparser
import recognize_configuration
from voice_recognition.auth import authorization_metadata
from voice_recognition.common import build_recognition_request


def _construct_config(audio_file):
    """
        Конструирование объекта конфигурации распознавания речи
        Params:
            audio_file - аудиофайл в формате который требуется распознать
        Return:
            RecognizeConfiguration - объект конфигурации
    """
    config = configparser.ConfigParser()
    config.read('recognize.ini')
    api_key = config['Authorization']['ApiKey']
    secret_key = config['Authorization']['SecretKey']
    return recognize_configuration.RecognizeConfiguration(api_key=api_key,
                                                          secret_key=secret_key,
                                                          rate=audio_file.frame_rate,
                                                          num_channels=audio_file.channels)


def recognize(audio_file):
    """
        Распознавание речи
        Params:
            audio_file - аудиофайл который требуется распознать
        Return:
            str - распознанный текст
    """
    config = _construct_config(audio_file)
    metadata = authorization_metadata(config.api_key, config.secret_key, "tinkoff.cloud.stt", type=dict)
    request_body = build_recognition_request(config, audio_file, type="json")
    response = requests.post(f"https://{config.endpoint}/v1/stt:recognize", json=request_body, headers=metadata)
    if response.status_code != 200:
        raise RuntimeError(f"""REST failed with HTTP code {response.status_code}
                               Headers: {response.headers}
                               Body: {response.text}""")
    recognition_result = response.json()
    return recognition_result.get("Transcription")
