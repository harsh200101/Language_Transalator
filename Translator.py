from textblob import TextBlob   # For transcription
import speech_recognition as sr  # Listening
from tkinter import *  # To create window

root = Tk()
root.geometry('500x500')
root.title('Transcript')

var = StringVar()
var.set("no_default")

def rowCol(languange, code, row):
    radio = Radiobutton(root, text = languange, variable = var, value = code).grid(row = row, column = 0, padx = 50, sticky = W)

result = Text(root, width = 30)

def speak():
    print(var.get()) 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
        except:
            text = '\nTry Again!\n'
    tb = TextBlob(text)
    try:
        t = tb.translate(to = var.get())
    except:
        t = text
    # tb.translate(from_lang=, to=)
    # Label(root, text = str(t)).grid(row = 11, column = 1)
    result.insert(END, str(t) + " ")

rowCol('Hindi', 'hi', 0)
rowCol('Sanskrit', 'sa', 1)
rowCol('English', 'en', 2)
rowCol('Telgu', 'te', 3)
rowCol('French', 'fr', 4)
rowCol('German', 'de', 5)
rowCol('Gujrati', 'gu', 6)
rowCol('Japanese', 'ja', 7)
Label(root, text = "___________").grid(row = 8)
Button(root, text = 'Speak Now', command = speak).grid(row = 9, column = 0)
result.grid(row = 1, column = 3, padx = 30, rowspan = 8)

root.mainloop()