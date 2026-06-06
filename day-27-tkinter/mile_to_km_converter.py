from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(100, 100)
window.config(padx=20, pady=20)

input = Entry(width=10)
input.grid(column=1, row=0)

miles = Label(text="miles")
miles.grid(column=2, row=0)

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

def convert_miles_to_km():
    miles = float(input.get())
    km = miles * 1.60934
    result_label.configure(text=str(km))


calc_button = Button(text="Calculate", command =convert_miles_to_km)
calc_button.grid(column=1, row=2)

window.mainloop()
