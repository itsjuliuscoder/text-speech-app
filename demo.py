from gtts import gTTS  # type: ignore
import os

text = open('demo.txt', 'r').read()

language = 'fr'
output = gTTS(text=text, lang=language, slow=False).save("audio.mp3")

os.system("afplay audio.mp3")