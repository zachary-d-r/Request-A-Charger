import eel
import os

class student:
    
    # Information we need from the student
    studentID = ''
    email = ''
    name = ''

    def __init__(self, path='', backend=True):
        
        # Check to see if the program is in the backend or not
        if backend == False:
            with open('output.txt', 'w') as f:
                f.write("NONE")
            return
        # Make sure there is a path to an output file
        if path == '':
            return
        
        # Read the output file
        with open('output.txt', 'r') as f:
            contents = f.readlines()

        # Restart the program if nothing is in the file
        if contents == ["NONE"]:
            open('output.txt', 'w').write('NONE')

            os.system("python backend.py")
            exit()

        # Attatch all given information to the correct variables
        if len(contents) >= 1: self.studentID = contents[0].split('\n')[0]
        if len(contents) >= 2: self.email = contents[1].split('\n')[0]
        if len(contents) >= 3: self.name = contents[2].split('\n')[0]

    # Load all info into output.txt for another program to read it
    def loadIntoFile(self, ID = '', email = '', name = ''):
        with open('output.txt', 'w') as f:
            toWrite = ''

            if ID    != '': toWrite += f'{ID}\n'
            if name  != '': toWrite += f'{name}\n'
            if email != '':  toWrite += f'{email}\n'

            f.write(f"{toWrite}")


