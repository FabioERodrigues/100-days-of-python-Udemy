BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random




window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
to_learn = {}
text = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    org_data = pandas.read_csv("data/french_words.csv")
    to_learn = org_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# Random words
def random_words():
    # CSv
    global text, timer
    window.after_cancel(flip_card)
    text = random.choice(to_learn)
    canvas.itemconfig(card, image=card_front)
    canvas.itemconfig(title, text="French", fill="#000000")
    canvas.itemconfig(handle, text=text["French"], fill="#000000")
    window.after(3000, flip_card)

# english
card_back = PhotoImage(file="images/card_back.png")
def flip_card():

    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(handle, text=text["English"], fill="white")


# remove
def remove():
    to_learn.remove(text)
    to_learn_csv = pandas.DataFrame(to_learn)
    to_learn_csv.to_csv("data/words_to_learn.csv", index=False)
    random_words()
# UI
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
handle = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR,  highlightthickness=0)
canvas.grid(row=0, column=0,  columnspan=2)

#
# button_back = Button(image=card_back, padx=50,pady=50, width=800, height=526)
# button_back.grid(row=0, column=1, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_image, highlightthickness=0,command=random_words)
button_wrong.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
button_right = Button(image=right_image, highlightthickness=0,command=remove)
button_right.grid(row=1, column=1)

random_words()


window.mainloop()
