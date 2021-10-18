import eel
import os
import pandas as pd

class student:
    
    # Information we need from the student
    email = ''
    charger = 0
    animate = False

    def setEmail(self, inputEmail):
        self.email = f'{inputEmail}@emeryweiner.org'

    # Change the charger to a human readable format
    def readCharger(self):
        if self.charger == 0: return 'User has not chosen a charger'
        elif self.charger == 1: return 'User chose: USB-C'
        elif self.charger == 2: return 'User chose: MagSafe 2'
        elif self.charger == 3: return 'User chose: Lightning'
        elif self.charger == 4: return 'User chose: Windows Surface'