from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(',')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter_list + symbol_list + number_list
    shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website:{
            "email": email,
            "password": password
        }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo("OOPS", "Please make sure you haven't left any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as data:
                #reading data
                data = json.load(data)
        except FileNotFoundError:
            with open("data.json", mode="w") as data:
                json.dump(new_data, data, indent=4)
        else:
            #updating old data with new data
            data.update(new_data)
            with open("data.json", mode="w") as data:
                #saving updated data
                json.dump(new_data, data, indent=4)
        finally:
                website_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def find_password():
    website = website_input.get()
    try:
        with open("data.json", mode="r") as data:
            data = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo("OOPS", "no data found")
    else:
        if website in data:
            messagebox.showinfo("Password Found", f"{website}\nemail:{data[website]['email']}\npassword:{data[website]['password']}")
        else:
            messagebox.showinfo("Error", f"No detail for {website} exists")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.geometry("600x600")
window.configure(background="white")
window.config(padx=50, pady=50)



canvas = Canvas(width=200, height=200, background="white", highlightthickness=0)
logo_img =PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:",background="white")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:",background="white")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:",background="white")
password_label.grid(row=3, column=0)
website_input = Entry(width=31)
website_input.grid(row=1, column=1)
website_input.focus_set()
email_input = Entry(width=50)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "@gmail.com")
password_input = Entry(width=31)
password_input.grid(row=3, column=1)
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2)


















window.mainloop()