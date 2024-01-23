import math
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
times = None


def stop_timer():
    window.after_cancel(times)
    timer.config(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
    canvas.itemconfig(time, text="00:00")
    lab.config(text="")


def start_timer():
    global reps
    reps += 1

    work_sec = 60 * WORK_MIN
    short_break_sec = 60 * SHORT_BREAK_MIN
    long_break_sec = 60 * LONG_BREAK_MIN

    if reps % 8 == 0:
        timer.config(text="Break", fg=RED, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer.config(text="Break", fg=PINK, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
        count_down(short_break_sec)
    else:
        count_down(work_sec)
        timer.config(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)


def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(time, text=f"{count_min}:{count_sec}")
    if count > 0:
        global times
        times = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mar = ""
        work_session = math.floor(reps/2)
        for n in range(work_session):
            mar += "✓"
        lab.config(text=mar)


window = Tk()
window.title("pomodoro")

window.config(pady=50, padx=100, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
time = canvas.create_text(100, 130, text="00.00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
timer.grid(column=1, row=0)

button_1 = Button(text="Start", command=start_timer)
button_1.grid(row=2, column=0)

button_2 = Button(text="Reset", command=stop_timer)
button_2.grid(row=2, column=2)

lab = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
lab.grid(row=3, column=1)

window.mainloop()
