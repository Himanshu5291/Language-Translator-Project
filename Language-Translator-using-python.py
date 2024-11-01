#  pip install googletrans-3.0.0.tar.gz
import os
from tkinter import PhotoImage, Tk, Label, Entry, Button, StringVar, OptionMenu
from googletrans import Translator
from gtts import gTTS

window = Tk()
window.title("Language Translator")
window.geometry("626x399")
window.config(bg="black")
set_bg = PhotoImage(file="C:/Users/Himanshu/Downloads/abstract-uv-ultraviolet-light-composition.png")

label_1= Label(window, image=set_bg)
label_1.place(x=0, y=0)

e1 = Entry(window, bg="white", fg="black", font=("Arial", 25, "bold"))
e1.place(x=30, y=30)

def convert_language():
    
    a1 = e1.get()
    t1 = Translator()
    t2 = click_option.get()

    if t2 == "English":
        convert = "en"
    elif t2 == "Hindi":
        convert = "hi"
    elif t2 == "Germany":
        convert = "de"
    elif t2 == "Russian":
        convert = "ru"
    elif t2 == "Japanese":
        convert = "ja"
    elif t2 == "Spanish":
        convert = "es"
    elif t2 == "French":
        convert = "fr"
    elif t2 == "Korean":
        convert = "ko"
    elif t2 == "Chinese":
        convert = "zh-CN"
    elif t2 == "Telugu":
        convert = "te"

    trans_text = t1.translate(a1, dest=convert)
    trans_text = trans_text.text
    ob1 = gTTS(text=trans_text, lang=convert, slow=False)
    label_2.config(text=trans_text)

choices = [
    "English",
    "Hindi", 
    "Germany", 
    "Russian", 
    "Japanese", 
    "Spanish", 
    "French",
    "Korean",
    "Chinese",
    "Telugu"
]

click_option = StringVar()
click_option.set("Select Language")

list_drop = OptionMenu(window, click_option, *choices)
list_drop.config(background="green",foreground="white", font=("Arial", 15, "bold"))
list_drop.place(x=400, y=30)

label_2 = Label(window, text="\t\t\t\t\t\t", bg="black", fg="white", font=("Arial", 40, "bold"))
label_2.place(x=0, y=180)
label_2 = Label(window, text="Translated Text", bg="black", fg="white", font=("Arial", 40, "bold"))
label_2.place(x=120, y=180)

Button_1 = Button(window, text="Translate", bg="red", fg="white", font=("Arial", 25, "bold"), command=convert_language)
Button_1.place(x=220, y=300)

window.mainloop()