import eel
import os

class student:
    
    # Information we need from the student
    email = ''
    name = ''
    charger = 0

    def setEmail(self, inputEmail):
        self.email = f'{inputEmail}@emeryweiner.org'

    # Change the charger to a human readable format
    def readCharger(self):
        if self.charger == 0: return 'User has not chosen a charger'
        elif self.charger == 1: return 'User chose: USB-C'
        elif self.charger == 2: return 'User chose: MagSafe 2'
        elif self.charger == 3: return 'User chose: Lightning'
        elif self.charger == 4: return 'User chose: Windows Surface'