import eel
import os

class student:
    
    # Information we need from the student
    studentID = ''
    email = ''
    name = ''

    def __init__(self):
        print("Student object created")

    # Load all info into output.txt for another program to read it
    def loadIntoFile(self, ID = '', email = '', name = ''):
        with open('output.txt', 'w') as f:
            toWrite = ''

            if ID    != '': toWrite += f'{ID}\n'
            if name  != '': toWrite += f'{name}\n'
            if email != '':  toWrite += f'{email}\n'

            f.write(f"{toWrite}")
