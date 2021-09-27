import eel
import os

class student:
    
    # Information we need from the student
    email = ''
    name = ''
    charger = 0

    def setEmail(self, inputEmail):
        self.email = f'{inputEmail}@emeryweiner.org'