from tkinter import *
from words import words
import random


def start_function(input_field, NUMBER_OF_WORDS, canvas, canvas_text, timer):
    """Generates set of words, prints it on the canvas and starts the timer"""
    global random_200_words_string, random_200_words_list
    input_field.delete(1.0, END)
    random_200_words_list = random.choices(words, k=NUMBER_OF_WORDS)
    random_200_words_string = " ".join(random_200_words_list)
    canvas.itemconfigure(canvas_text, text=random_200_words_string, font='Helvetica 18 normal')
    timer_function(timer)


def timer_function(timer):
    try:
        timer.start()
    except RuntimeError:
        timer.reset()


def result_function(timer, input_field, canvas, canvas_text, TIME_LIMIT):
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


def reset_function(timer, input_field, canvas, canvas_text, WELCOME_SCREEN_TEXT):
    timer.cancel()
    input_field.delete(1.0, END)
    canvas.itemconfigure(canvas_text, text=WELCOME_SCREEN_TEXT, font='Helvetica 18 normal')
