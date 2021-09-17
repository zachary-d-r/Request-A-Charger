import Student
import eel

student = Student.student()  # Create student object to load file

eel.init('web')  # Initialize the app

# Function to print a return value from js
def printReturn(n):
        print(n)

# Function to get student id when the submit button is clicked
@eel.expose
def getStudentEmail():
    eel.getStudentIDJS()()  # The () after the function gets the return values
    student.email = eel.getStudentIDJS()()

    print(f'{student.email}')


eel.start('index.html')  # Start the app
