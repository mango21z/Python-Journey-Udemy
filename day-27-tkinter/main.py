from tkinter import *

def my_button_clicked():
    print("i got clicked")
    my_label["text"] = label.get()

window = Tk()
window.title("first GUI Program")
window.minsize(400, 300)
window.config(padx=20, pady=20)

#label
my_label = Label(text="Hello World", font=("Arial", 25, "bold"))

my_label["text"] = "My car"
my_label.grid(column=0, row=0)

#button



button = Button(text="click me",command=my_button_clicked)
button.grid(column=1, row=1)

#label
label = Entry(width=35)
label.grid(column=2, row=1)










window.mainloop()