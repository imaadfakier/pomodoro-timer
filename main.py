import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# WORK_MIN = 20
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20
WORK_MIN = 120
SHORT_BREAK_MIN = 60
LONG_BREAK_MIN = 90

reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    # global timer  # usage: testing purposes
    global reps, timer
    window.after_cancel(timer)
    # global reps, timer
    # reps = 0
    # timer = 0
    reps, timer = 0, None
    # timer_text.config(text='00:00')  # will throw error
    canvas.itemconfig(tagOrId=timer_text, text='00:00')
    timer_label.config(text='Timer')
    checkmark_label.config(text='')


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    # count_down(5)
    # count_down(5 * 60)

    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # while reps != 8:
    #     if reps % 2 > 0:
    #         # if it's the 1st/3rd/5th/7th rep:
    #         count_down(work_sec)
    #     # elif reps == 8:
    #     elif reps % 8 == 0:
    #         # if it's the 8th rep:
    #         count_down(long_break_sec)
    #     elif reps % 2 == 0:
    #         # if its the 2nd/4th/6th rep:
    #         count_down(short_break_sec)
    if reps % 2 > 0:
        # if it's the 1st/3rd/5th/7th rep:
        count_down(work_sec)
        timer_label['text'] = 'Work'
        timer_label.config(fg=GREEN)
    # elif reps == 8:
    elif reps % 8 == 0:
        # if it's the 8th rep:
        count_down(long_break_sec)
        timer_label['text'] = 'Long Break'
        timer_label.config(fg=RED)
    elif reps % 2 == 0:
        # if its the 2nd/4th/6th rep:
        count_down(short_break_sec)
        timer_label['text'] = 'Short Break'
        timer_label.config(fg=PINK)
    else:
        return


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title(string='Pomodoro')
# window.config(padx=100, pady=50)
window.config(padx=100, pady=50, bg=YELLOW)

# labels
timer_label = tkinter.Label(text='Timer', font=(FONT_NAME, 36, 'bold'), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

# checkmark_label = tkinter.Label(text='✔', font=(FONT_NAME, 8, 'bold'), bg=YELLOW, fg=GREEN)
checkmark_label = tkinter.Label(font=(FONT_NAME, 8, 'bold'), bg=YELLOW, fg=GREEN)
# checkmark_label['pady'] = 15
checkmark_label.grid(column=1, row=3)

# buttons
# start_button = tkinter.Button(text='Start')
# start_button = tkinter.Button(text='Start', highlightthickness=0)
start_button = tkinter.Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# reset_button = tkinter.Button(text='Reset')
# reset_button = tkinter.Button(text='Reset', highlightthickness=0)
reset_button = tkinter.Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# creating a canvas (i.e. the canvas widget); width and height are in pixels
# canvas = tkinter.Canvas(width=200, height=224)
# canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW)
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_photo = tkinter.PhotoImage(file='./tomato.png')
# canvas.create_image(100, 112, image=tomato_photo)  # centering tomato image
# canvas.create_image(102, 112, image=tomato_photo)  # to prevent part of tomato image
                                                   # being cut off
canvas.create_image(100, 112, image=tomato_photo)
# canvas.create_text(102, 112, text='00:00')
# canvas.create_text(102, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
# canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
# canvas.pack()
canvas.grid(column=1, row=1)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# due to GUIs being event-driven (through the .mainloop()) where, after every
# fraction of a second, the GUI will check to see if anything happened (i.e. a button
# click or any other event(s) that might've gone/fired off etc.) meaning the idea
# below is not a viable one as, when you try to run the program, the program won't
# run
# import time
#
# count = 5
#
# while True:
#     time.sleep(1)
#     count -= 1


# quick examples
# def say_something(thing):
#     print(thing)
# def say_something(a, b, c):
#     print(a)
#     print(b)
#     print(c)
def count_down(count):
    # print(count)
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = '0{}'.format(count_min)
    if count_sec == 0:
        # works due to dynamic typing concept; the ability to change a variable's
        # data type by changing the content in the given variable like so: a =
        # 'Hello' -> a = 4 further demonstrating Python's uniqueness since on the
        # one hand, it is strongly typed in the sense that it holds on to the data
        # type of the given variable so, for example, a = 'Hello' is a variable of
        # type str and if you try to do or carry out operations with this (variable
        # of type) str that you're not supposed to like a ** 2 - an error will be
        # thrown - similarly if you tried to do pow(a, 3) - an error will be thrown
        # - this means that or is where a language(, Python - the best language -
        # in our case,) is strongly typed
        count_sec = '00'  # using the concept of dynamic typing to change the data
                          # type of count_sec from a variable of type str to a variable
                          # of type int
    elif count_sec < 10:
        # count_sec = '0'.join(str(count_sec))
        # count_sec = '0' + str(count_sec)
        # count_sec = '0{}'.format(count_sec)
        count_sec = f'0{count_sec}'
    # canvas.itemconfig(tagOrId=timer_text, text=count)
    canvas.itemconfig(tagOrId=timer_text, text='{minutes}:{seconds}'.format(minutes=count_min, seconds=count_sec))
    # canvas.itemconfig(tagOrId=timer_text, text=f'{count_min}:{count_sec}')
    if count == 0:
        # return
        # start_timer()
        # return
        if reps % 2 > 0:
            checkmark_label['text'] += '✔'
        # marks = ''
        # work_sessions = math.floor(reps / 2)
        # for _ in range(work_sessions):
        #     marks += '✔'
        # checkmark_label.config(text=marks)
        start_timer()
        return
    # window.after(1000, count_down, count - 1)
    global timer
    timer = window.after(1000, count_down, count - 1)

# window.after(1000, say_something, 'I\'m the thing')  # 1000 ms = 1 second
# window.after(1000, say_something, 3, 5, 8)
# count_down(5)


window.mainloop(n=0)
