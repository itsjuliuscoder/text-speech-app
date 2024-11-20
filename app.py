from gtts import gTTS  # type: ignore
import os
from tkinter import *

root = Tk()

canvas = Canvas(root, width=400, height=300)
canvas.pack()
root.title("Text to Speech App")

def textToSpeech():
    text = entry.get()
    language = 'en'
    output = gTTS(text=text, lang=language, slow=False)
    output.save("audio.mp3")
    os.system("afplay audio.mp3")

entry = Entry(root)
canvas.create_window(200, 180, window=entry)

title = Label(text="Hello, Julius!", font=("Poppins", 20, "bold"))
canvas.create_window(200, 100, window=title)
title = Label(text="Enter a text you want to hear", font=("Arial", 14 ))
canvas.create_window(200, 140, window=title)

button = Button(text='Convert', command=textToSpeech)
canvas.create_window(200, 230, window=button)

root.mainloop()