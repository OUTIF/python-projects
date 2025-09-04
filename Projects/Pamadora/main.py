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
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(str(timer))
    canvas.itemconfig(timer_text, text='00:00')
    checkmark_label.config(text='')
    Timer_label.config(text='Timer', fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        count_down(long_break_sec)
        Timer_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        Timer_label.config(text='Break', fg=PINK)
    else:
        count_down(work_sec)
        Timer_label.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global checkmark_label
    count_min = math.floor(count/60)
    count_sec = (count % 60)
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ''
        work_session=math.floor(reps/2)
        for index in range(work_session):
            marks +='✓'
            checkmark_label.config(text=marks)




# ---------------------------- UI SETUP ------------------------------- #


#window
window = Tk()
window.title('pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


#canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pamodoro_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=pamodoro_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=("Courier", 35, 'bold'))
canvas.grid(row=1, column=1)



#labels
Timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW ,font=("Courier", 35, 'bold'))
Timer_label.grid(row=0, column=1)

checkmark_label =Label(fg=GREEN, bg=YELLOW,font=("Courier", 20, 'bold'))
checkmark_label.grid(row=3, column=1)



#buttons
start_button = Button(text='start',background=YELLOW,command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='reset', background=YELLOW,command=reset_timer)
reset_button.grid(row=2, column=3)





window.mainloop()
