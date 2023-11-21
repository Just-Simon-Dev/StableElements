import sys
import os
from colors.bcolor import bcolors
import keyboard
import time
from data_visualisation.all_elements_visualisation import start_all_elements_visualisation 
from data_visualisation.dataset_visualisation import start_dataset_visualisation
from data_visualisation.model_prediction_visualisation import start_model_prediction_visualisation
from generating_models.generate_model import generate_model
from testing_models.test_model import start_testing
from ui import uimanager


if __name__ == "__main__":
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    uimanager.clean()
    print(f"{bcolors.OKBLUE}Hello to our project we are happy that you are here.")
    print(f"{bcolors.OKBLUE}This is the ai that predicts if the element is radioactive or not.")
    print(f"{bcolors.OKBLUE}To exit our project press esc")
    
    while True:
        
        question = "Select what you want to do: "
        choices = ["visualise data", "generate model", "test model"]
        
        choice = uimanager.make_choice(question, choices)
        
        # test model
        if(choice == 2):
            print(f"{bcolors.OKBLUE}Let's test our model!")
            
            selected_model = uimanager.choice_of_models()
            
            start_testing(selected_model)
            
            
        
        # generate model
        
        if(choice == 1):
            for i in range(1):
                input()
                uimanager.clean()
            
            print(f"{bcolors.OKBLUE}Let's generate a wonderful ai model!")
            print(f"{bcolors.WARNING}For now we did not implement to get your own dataset, we are sorry for that.\n\n")
            
            iterations = int(input(f"{bcolors.OKBLUE}For how many models we should choose the best one?: {bcolors.OKGREEN}"))
            
            generate_model(iterations)
        
        # data visualisation
        if(choice == 0):
            print(f"{bcolors.OKBLUE}Let's make some visualisations!")
            question = "Please select what you want to visualise"
            choices = ["all elements visualisation", "dataset visualisation", "model predictions visualisation"]
        
            choice = uimanager.make_choice(question, choices)
            
            # dataset visualisation
            if choice == 0:
                start_all_elements_visualisation()
            
            # dataset visualisation
            if choice == 1:
                start_dataset_visualisation()
            
            # model predictions visualisation
            if choice == 2:
                print(f"{bcolors.OKBLUE}Let's show the predictions of model!")
                
                selected_model = uimanager.choice_of_models()
                
                start_model_prediction_visualisation(selected_model)
                
        
        
        
        
        