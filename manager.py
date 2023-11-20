import os
from colors.bcolor import bcolors
import keyboard
import time
from data_visualisation.visualize_dataset import start 
from generating_models.generate_model import generate_model
from testing_models.test_model import start_testing

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
        clean()

if __name__ == "__main__":
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

    print(f"{bcolors.OKBLUE}Hello to our project we are happy that you are here.")
    print(f"{bcolors.OKBLUE}This is the ai that predicts if the element is radioactive or not.")
    
    question = "To begin select what you want to do: "
    choices = ["visualise data", "generate model", "test model"]
    
    choice = make_choice(question, choices)
    
    # data visualisation
    if(choice == 0):
        print(f"{bcolors.OKBLUE}Let's make some visualisations!")
        question = "Please select what you want to visualise"
        choices = ["dataset visualisation", "model predictions visualisation"]
    
        choice = make_choice(question, choices)
        
        # dataset visualisation
        if choice == 0:
            start()
        
        # model predictions visualisation
        if choice == 1:
            print(f"{bcolors.FAIL}Not implemented!")
            pass
    
    # generate model
    
    if(choice == 1):
        for i in range(1):
            input()
            clean()
        
        print(f"{bcolors.OKBLUE}Let's generate a wonderful ai model!")
        print(f"{bcolors.WARNING}For now we did not implement to get your own dataset, we are sorry for that.\n\n")
        
        iterations = int(input(f"{bcolors.OKBLUE}For how many models we should choose the best one?: {bcolors.OKGREEN}"))
        
        generate_model(iterations)
        
    
    # test model
    if(choice == 2):
        print(f"{bcolors.OKBLUE}Let's test our model!")
        
        question = "Please select the model to test"
        choices = os.listdir("models")
    
        choice = make_choice(question, choices)
        
        selected_model = choices[choice]
        
        start_testing(selected_model)
        
        
        
        
        