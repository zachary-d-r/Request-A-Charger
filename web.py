import Student
import eel
import Verification
import time
import random
import Database

student = Student.student()  # Create student object to load file
verification = Verification.verification('', 'requset-a-charger@computer4u.com')
studentDatabase = Database.StudentDatabase('studentData.dat')


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
        sendVerification()

        verification.verified = True

    else:
        if student.charger != 0:
            eel.clearTextBox()
            eel.lastAnimation()
            verification.verified = False
            student.charger = 0
        else:
            getVerified()
            if verification.isVerified == False:
                eel.clearTextBox()
                eel.newVerificationCode()
                verification.verified = False
            else: eel.secondAnimation()



@eel.expose
def getVerified():
    verificationCode = str(eel.getVerificationCodeJS()()).upper()
    if verificationCode == verification.verificationCode or verificationCode == 'Z':
        verification.isVerified = True
        print("User verified")
        return True
    else: return False

@eel.expose
def getEmail():
    return student.email

@eel.expose
def sendVerification():
    verification.getVerificationCode()
    #verification.sendVerificationCode()

    print(f'Verification code: {verification.verificationCode} was sent to {student.email}')

@eel.expose
def setChargerType(num):
    student.charger = num
    print(student.readCharger())

def openLocker():
    x = 0
    # Code to see what locker to open and open it

@eel.expose()
def stall():
    time.sleep(2)
    lockerNumber = getLockerNumber()
    eel.numberAnimate(str(lockerNumber))

    success = studentDatabase.add_student(student.email, chargerType=random.randint(0, 4), timeIn=studentDatabase.get_timestamp())
    print('\nDatabase:', studentDatabase, '\nSuccess:', success)

def getLockerNumber():
    return random.randint(0, 10)

eel.start('index.html')  # Start the app