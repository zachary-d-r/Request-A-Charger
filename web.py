import Student
import eel
import Verification

student = Student.student()  # Create student object to load file
verification = Verification.verification('esfgn', 'sadfn')

eel.init('web')  # Initialize the app

# Function to print a return value from js
def printReturn(n):
        print(n)

# Function to get student id when the submit button is clicked
@eel.expose
def getStudentEmail():
    eel.getStudentEmailJS()()  # The () after the function gets the return values
    student.email = eel.getStudentEmailJS()()

    print(f'{student.email}')

    # Send email
    verification.getVerificationCode()
    print(verification.verificationCode)


eel.start('index.html')  # Start the app
