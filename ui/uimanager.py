import sys
import os
from colors.bcolor import bcolors
import keyboard
import time

def exit_program():
    clean()
    print(f"{bcolors.WARNING}exiting the program...")
    exit()

def clean():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')


    # For macOS and Linux
    else:
        _ = os.system('clear')

def make_choice(question:str, choices: list[str], selected_choice:int = 0):
    while True:
        time.sleep(0.1)
        print(f"{bcolors.OKBLUE}{question}")
        for idx, choice in enumerate(choices):
            print(f"{bcolors.OKBLUE}> {choice}") if idx != selected_choice else print(f"{bcolors.OKGREEN}> {choice}")
        key = keyboard.read_key()
        if key == keyboard.KEY_UP:
            selected_choice = selected_choice-1 if selected_choice != 0 else 0
        if key == keyboard.KEY_DOWN:
            selected_choice = selected_choice+1 if selected_choice != len(choices) - 1 else len(choices) - 1
        if key == 'enter':
            clean()
            return selected_choice
        if key == 'esc':
            exit_program()
        clean()

def choice_of_models():
    question = "Please select the model to test"
    choices = os.listdir("models")

    choice = make_choice(question, choices)
    
    selected_model = choices[choice]
    
    return selected_model