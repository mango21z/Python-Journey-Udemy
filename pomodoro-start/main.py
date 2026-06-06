from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    if TIMER is not None:
        window.after_cancel(TIMER)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text = "00:00")
    check_label.config(text="")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def bring_to_front():
    # Make window topmost temporarily
    window.attributes('-topmost', True)
    window.update()
    # Disable topmost so it behaves normally afterward
    window.attributes('-topmost', False)


def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if REPS % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)
    elif REPS % 2 == 1:
        countdown(work_sec)
        timer_label.config(text="Work")
        bring_to_front()
    elif REPS % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
        bring_to_front()





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec =f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, countdown, count-1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(REPS / 2)
        for _ in range(work_session):
            mark += "✔"
            check_label.config(text =mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img =PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 40, "bold"))
canvas.grid(row=1, column=1)


timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(row=2, column=1)
timer_label.grid(row=0, column=1)

start_btn = Button(text="Start", command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", command=reset_timer)
reset_btn.grid(row=2, column=2)

check_label = Label(bg=YELLOW,fg=GREEN, font=(FONT_NAME, 10, "bold"))
check_label.grid(row=3, column=1)











window.mainloop()