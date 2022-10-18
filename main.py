from tkinter import *
import customtkinter
from words import words
import random
from resettabletimer import ResettableTimer

NUMBER_OF_WORDS = 150
TIME_LIMIT = 60
WELCOME_SCREEN_TEXT = f"Welcome to the typing speed test.\n\nThe average typing speed is around 40 words per minute. " \
                      f"Let's see how fast you are.\nAfter clicking the 'Start Test' button, {NUMBER_OF_WORDS} random " \
                      f"words selected from the 1000 most used English words will appear in the top box. At that " \
                      f"moment the timer starts running and you have {TIME_LIMIT} seconds to type as many words as " \
                      f"possible in the bottom box.\nWhen your time's up, your result will be displayed. "


def start_function():
    """Generates set of words, prints it on the canvas and starts the timer"""
    global random_200_words_string, random_200_words_list
    input_field.delete(1.0, END)
    random_200_words_list = random.choices(words, k=NUMBER_OF_WORDS)
    random_200_words_string = " ".join(random_200_words_list)
    canvas.itemconfigure(canvas_text, text=random_200_words_string, font='Helvetica 18 normal')
    timer_function()


def timer_function():
    """Starts and restarts the timer"""
    try:
        timer.start()
    except RuntimeError:
        timer.reset()


def result_function():
    """Stops timer, calculates result and prints it on the canvas"""
    global random_200_words_list, score
    score = 0
    timer.cancel()
    input_text = input_field.get(1.0, END)
    input_text_list = input_text.split()
    for number in range(len(input_text_list)):
        if input_text_list[number] == random_200_words_list[number]:
            score += 1
    canvas.itemconfigure(canvas_text, text=f"Your result is {score} words per {TIME_LIMIT} seconds.",
                         font='Helvetica 28 normal')


def reset_function():
    timer.cancel()
    input_field.delete(1.0, END)
    canvas.itemconfigure(canvas_text, text=WELCOME_SCREEN_TEXT, font='Helvetica 18 normal')


timer = ResettableTimer(TIME_LIMIT, result_function)

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

window = Tk()
window.title("Typing Speed Test")
window.config(padx=50, pady=50)

canvas = Canvas(master=window, width=600, height=300, highlightthickness=0, background="white")
canvas_text = canvas.create_text(20, 10, text=WELCOME_SCREEN_TEXT, font='Helvetica 18 normal', width=560, anchor="nw")
canvas.pack()

input_field = Text(master=window, width=85)
input_field.pack(pady=(20, 20))

start_button = customtkinter.CTkButton(master=window, text="Start Test", fg_color='#77dd77', hover_color="#67c267",
                                       width=130, command=start_function)
start_button.pack(pady=(0, 20))

reset_button = customtkinter.CTkButton(master=window, text="Reset", fg_color='#FF6666', hover_color="#d95555",
                                       width=130, command=reset_function)
reset_button.pack()

window.mainloop()
