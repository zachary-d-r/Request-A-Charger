import eel
import os

class student:
    
    # Information we need from the student
    email = ''
    name = ''

    def setEmail(self, inputEmail):
        self.email = f'{inputEmail}@emeryweiner.org'