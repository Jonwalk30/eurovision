from gtts import gTTS
from pygame import mixer
from mutagen.mp3 import MP3
import time


def save(name: str, text: str, language: str, slow: bool = False):
    tts = gTTS(text=text, lang=language, slow=slow)
    with open(name, 'wb') as f:
        tts.write_to_fp(f)


def play(file: str):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    print()
    audio = MP3(file)
    time.sleep(audio.info.length)
