import Student
import eel
import Verification

student = Student.student()  # Create student object to load file
verification = Verification.verification('', 'requset-a-charger@computer4u.com')


eel.init('web')  # Initialize the app

# Function to print a return value from js
def printReturn(n):
        print(n)

# Function to get student id when the submit button is clicked
@eel.expose
def getStudentEmail():
    if verification.verified == False:
        eel.getStudentEmailJS()()  # The () after the function gets the return values
        student.setEmail(eel.getStudentEmailJS()())
        eel.clearTextBox()

        verification.toAddress = student.email

        # Send email
        verification.getVerificationCode()
        #verification.sendVerificationCode()

        print(f'Verification code: {verification.verificationCode} was sent to {student.email}')

        verification.verified = True

    else:
        getVerificationCode()

        # Trigger a new animation

@eel.expose
def getVerificationCode():
    verificationCode = str(eel.getVerificationCodeJS()()).upper()
    if verificationCode == verification.verificationCode:
        print("User verified")
        return True

@eel.expose
def getEmail():
    return student.email

def openLocker():
    x = 0
    # Code to see what locker to open and open it


eel.start('index.html')  # Start the app