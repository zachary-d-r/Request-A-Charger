import eel
import os
import pandas as pd

class student:
    
    # Information we need from the student
    email = ''
    charger = 0
    animate = False
    deleted = False

    def setEmail(self, inputEmail):
        self.email = f'{inputEmail}@emeryweiner.org'

    # Change the charger to a human readable format
    def readCharger(self):
        charger_options = ('User has not chosen a charger', 'USB-C', 'MagSafe 2', 'Lightning', 'Windows Surface')

        # If the user did not return a charger, then return the first option
        if self.charger == 0: return charger_options[0]

        # Else, return a formatted string for the charger they chose
        else:
            return f'User chose: {charger_options[self.charger]}'