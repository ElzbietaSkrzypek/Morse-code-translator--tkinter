from morse_code import IMC
from tkinter import *
from PIL import Image, ImageTk
import pyperclip


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#913175"
LPINK = "#CD5888"
BLACK = '#400E32'
GREEN = "#9bdeac"
YELLOW = "#FFFBEB"
FONT_NAME = "Courier"


# ---------------------------- TRANSLATIONS DEFINITIONS ------------------------------- #

def normal_morse():
    message = ""
    user_input = var.get().lower()
    for char in user_input:
        for (key, values) in IMC.items():
            if char == key:
                message += values
                message += " "
    translation.config(text=message, fg="black", activeforeground=LPINK)
    pyperclip.copy(message)


def morse_normal():
    message = ""
    user_input = var.get().lower()
    words = user_input.split("/")
    signs = [word.split(" ") for word in words]
    for sign in signs:
        for i in sign:
            for (key, values) in IMC.items():
                if i == values:
                    message += key
        message += " "
    translation.config(text=message.upper(), fg="black", activeforeground=LPINK)
    # translation.insert(f"{message}")
    pyperclip.copy(message)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Morse Code Translator")
window.config(pady=50, padx=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = Image.open("morse-code.png")
resize_image = image.resize((125, 125))
morse_code_img = ImageTk.PhotoImage(resize_image)
canvas.create_image(100, 112, image=morse_code_img)
canvas.grid(row=1, column=1, columnspan=2)

# Labels

label_title = Label(text="Morse Code Translator", fg=PINK, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
label_title.grid(row=0, column=1)

Label(window, text="Provide your text to translate:", fg=LPINK, bg=YELLOW, font=(FONT_NAME, 16)).grid(
    row=3, column=1, columnspan=2)
Label(window, text='Type Morse Code using "." and "-", separate letters by space and words by "/".', fg=LPINK, bg=YELLOW, font=(FONT_NAME, 10)).grid(
    row=4, column=1, columnspan=2)
var = StringVar()
question = Entry(window, width=60, textvariable=var, fg=LPINK, bg=YELLOW, font=(FONT_NAME, 14))
question.grid(row=5, column=1, columnspan=2)

Label(window, text="Your translation:", fg=LPINK, bg=YELLOW, font=(FONT_NAME, 16)).grid(row=7, column=1,
                                                                                        columnspan=2)
translation = Label(window, text="", width=60, fg=LPINK, bg=LPINK, font=(FONT_NAME, 14), activeforeground=LPINK)
translation.grid(row=8, column=1, columnspan=2)

# Radio Button
rb_var = StringVar()
rb_normal_morse = Radiobutton(window, variable=rb_var, value="n-m", text="Normal -> Morse", fg=PINK, bg=YELLOW,
                              activebackground=LPINK, font=(FONT_NAME, 20))
rb_morse_normal = Radiobutton(window, variable=rb_var, value="m-n", text="Morse -> Normal", fg=PINK, bg=YELLOW,
                              activebackground=LPINK, font=(FONT_NAME, 20))
rb_var.set("n-m")
rb_normal_morse.grid(row=1, column=0)
rb_morse_normal.grid(row=1, column=3)


# Button

def translate():
    if StringVar.get(rb_var) == "n-m":
        normal_morse()
    else:
        morse_normal()


button_translate = Button(width=10, text="TRANSLATE", command=translate, fg=PINK, bg=YELLOW, activebackground=LPINK,
                          font=(FONT_NAME, 15))
button_translate.grid(row=6, column=1)


# ------------------------ WINDOW MAINLOOP--------------------- #
window.mainloop()
