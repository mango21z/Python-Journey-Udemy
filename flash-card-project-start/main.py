import pandas as pd
from tkinter import *
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
CURRENT_CARD = {}
to_learn = {}

# ---------------------------- READ DATA ------------------------------- #

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict("records")
else:
    to_learn = data.to_dict(orient="records")

# ---------------------------- BUTTONS ------------------------------- #
def next_card():
    global CURRENT_CARD, flip_timer
    window.after_cancel(flip_timer)
    CURRENT_CARD = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill = "black")
    canvas.itemconfig(card_word, text=CURRENT_CARD["French"], fill = "black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill= "white")
    canvas.itemconfig(card_word, text=CURRENT_CARD["English"],  fill= "white")
    canvas.itemconfig(card_background, image=card_back)

def is_known():
    to_learn.remove(CURRENT_CARD)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.configure(padx= 50, pady=50,background=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(window, width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 160,text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


right_image = PhotoImage(file="images/right.png")
known_button = Button(image=right_image, command=is_known)
known_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_image, command=next_card)
unknown_button.grid(row=1, column=0)

next_card()

window.mainloop()