from tkinter import *
from tkmacosx import Button
from words import words
import random
from resettabletimer import ResettableTimer


def start_function():
    global random_200_words_string, random_200_words_list
    input_field.delete(1.0, END)
    random_200_words_list = random.choices(words, k=150)
    random_200_words_string = " ".join(random_200_words_list)
    canvas.itemconfigure(canvas_text, text=random_200_words_string, font='Helvetica 18 normal')
    timer_function()


def timer_function():
    try:
        timer.start()
    except RuntimeError:
        timer.reset()


def result_function():
    global random_200_words_list, score
    score = 0
    timer.cancel()
    input_text = input_field.get(1.0, END)
    input_text_list = input_text.split()
    for each in range(len(input_text_list)):
        if input_text_list[each] == random_200_words_list[each]:
            score += 1
    canvas.itemconfigure(canvas_text, text=f"Your result is {score} words per minute.", font='Helvetica 28 normal')


def reset_function():
    timer.cancel()
    input_field.delete(1.0, END)
    canvas.itemconfigure(canvas_text, text=f"Welcome to the typing speed test.\n\nThe average typing speed is around "
                                           f"40 words per minute. Let's see how fast you are.\nAfter clicking the "
                                           f"'Start Test' button, 200 random words selected from the 1000 most "
                                           f"used English words will appear in the top box. At that moment the timer "
                                           f"starts running and you have one minute to type as many words as possible "
                                           f"in the bottom box.\nWhen your time's up, your result will be displayed.",
                         font=('Helvetica 18 normal'))


timer = ResettableTimer(60, result_function)

window = Tk()
window.title("Typing Speed Test")
window.config(padx=50, pady=50)

canvas = Canvas(window, width=600, height=300, highlightthickness=0, background="white")
canvas_text = canvas.create_text(20, 10, text=f"Welcome to the typing speed test.\n\nThe average typing speed is around "
                                           f"40 words per minute. Let's see how fast you are.\nAfter clicking the "
                                           f"'Start Test' button, 200 random words selected from the 1000 most "
                                           f"used English words will appear in the top box. At that moment the timer "
                                           f"starts running and you have one minute to type as many words as possible "
                                           f"in the bottom box.\nWhen your time's up, your result will be displayed.",
                                 font='Helvetica 18 normal', width=560, anchor="nw")
canvas.pack()

input_field = Text(window, width=85)
input_field.pack(pady=(20, 20))

start_button = Button(text="Start Test", bg='#77dd77', borderless=1, width=130, command=start_function)
start_button.pack(pady=(0, 20))

reset_button = Button(text="Reset", bg='#FF6666', borderless=1, width=130, command=reset_function)
reset_button.pack()

window.mainloop()
