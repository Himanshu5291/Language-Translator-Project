import os
from tkinter import PhotoImage, Tk, Label, Entry, Button, StringVar, OptionMenu
from gtts import gTTS
from transformers import MarianMTModel, MarianTokenizer

# Initialize Tkinter window
window = Tk()
window.title("Language Translator")
window.geometry("626x399")
window.config(bg="black")
set_bg = PhotoImage(file="C:/Users/Himanshu/Downloads/abstract-uv-ultraviolet-light-composition.png")

label_1 = Label(window, image=set_bg)
label_1.place(x=0, y=0)

e1 = Entry(window, bg="white", fg="black", font=("Arial", 25, "bold"))
e1.place(x=30, y=30)

# Translation function using Hugging Face's MarianMT
def convert_language():
    a1 = e1.get()
    t2 = click_option.get()

    # Mapping for language codes
    lang_map = {
        "English": "en",
        "Hindi": "hi",
        "Germany": "de",
        "Russian": "ru",
        "Italian": "it",
        "Spanish": "es",
        "French": "fr",
        "Arabic": "ar",
        "Chinese": "zh",
        "Dutch": "nl"
    }

    # Choose the corresponding language code
    if t2 in lang_map:
        target_lang = lang_map[t2]
    else:
        label_2.config(text="Invalid language")
        return

    # Load pre-trained MarianMT model for translation
    model_name = f'Helsinki-NLP/opus-mt-en-{target_lang}' if target_lang != 'en' else f'Helsinki-NLP/opus-mt-{target_lang}-en'
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)

    # Translate the input text
    translated = model.generate(**tokenizer(a1, return_tensors="pt", padding=True))
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)

    # Convert the translated text to speech
    ob1 = gTTS(text=translated_text, lang=target_lang, slow=False)
    ob1.save("translated_audio.mp3")
    os.system("start translated_audio.mp3")

    # Display the translated text in the GUI
    label_2.config(text=translated_text)

# Dropdown for selecting target language
choices = [
    "English",
    "Hindi", 
    "Germany", 
    "Russian",
    "Spanish", 
    "French",
    "Chinese",
    "Italian",
    "Arabic",
    "Dutch"
]

click_option = StringVar()
click_option.set("Select Language")

list_drop = OptionMenu(window, click_option, *choices)
list_drop.config(background="green", foreground="white", font=("Arial", 15, "bold"))
list_drop.place(x=400, y=30)

# Label to show translated text
label_2 = Label(window, text="Translated Text", bg="black", fg="white", font=("Arial", 40, "bold"))
label_2.place(x=120, y=180)

# Translate button
Button_1 = Button(window, text="Translate", bg="red", fg="white", font=("Arial", 25, "bold"), command=convert_language)
Button_1.place(x=220, y=300)

# Start the Tkinter event loop
window.mainloop()
