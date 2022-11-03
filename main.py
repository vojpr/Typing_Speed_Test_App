from tkinter import *
import customtkinter
from resettabletimer import ResettableTimer
from functions import result_function, start_function, reset_function

NUMBER_OF_WORDS = 150
TIME_LIMIT = 60
WELCOME_SCREEN_TEXT = f"\nWelcome to the typing speed test.\n\n\nAn average person can type 40 words per minute. " \
                      f"Let's check out your speed.\n\n{NUMBER_OF_WORDS} randomly chosen words from the 1000 most " \
                      f"frequently used English words will be displayed in this box when you click the 'Start Test' " \
                      f"button. At that moment the timer starts running and you have {TIME_LIMIT} seconds to type as " \
                      f"many words as you can in the bottom box.\nWhen your time's up, your result will be displayed. "

# Set up ResettableTimer
timer = ResettableTimer(TIME_LIMIT, lambda: result_function(timer, input_field, canvas, canvas_text, TIME_LIMIT))

# Set up Tkinter GUI window
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
window = Tk()
window.title("Typing Speed Test")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(master=window, width=600, height=300, highlightthickness=0, background="white")
canvas_text = canvas.create_text(20, 10, text=WELCOME_SCREEN_TEXT, font='Helvetica 18 normal', width=560, anchor="nw")
canvas.pack()

# Text field
input_field = Text(master=window, width=85)
input_field.pack(pady=(20, 20))

# Buttons
start_button = customtkinter.CTkButton(master=window, text="Start Test", fg_color='#77dd77', hover_color="#67c267", width=130,
                                       command=lambda: start_function(input_field, NUMBER_OF_WORDS, canvas, canvas_text, timer))
start_button.pack(pady=(0, 20))
reset_button = customtkinter.CTkButton(master=window, text="Reset", fg_color='#FF6666', hover_color="#d95555", width=130,
                                       command=lambda: reset_function(timer, input_field, canvas, canvas_text, WELCOME_SCREEN_TEXT))
reset_button.pack()

window.mainloop()
