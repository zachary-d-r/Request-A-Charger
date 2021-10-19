import Student
import eel
import Verification
import time
import random
import Database

student = Student.student()  # Create student object to store some info
verification = Verification.verification('', 'requset-a-charger@computer4u.com')  # Create verification object to email the verification code
studentDatabase = Database.StudentDatabase(r'Databases\studentData.dat')  # Create the student database

eel.init('web')  # Initialize the app

# Function to print a return value from js
def printReturn(n):
        print(n)

# Function to get student id when the submit button is clicked
@eel.expose
def getStudentEmail():
    if verification.verified == False:

        student.setEmail(eel.getStudentEmailJS()())  # Get the students email
        eel.clearTextBox()  # Clear the text box

        verification.toAddress = student.email  # Set the verification email to the students email
        sendVerification()  # Send email

        verification.verified = True  # A variable that proves the user has passed the first screen

    else:
        # Show the last screen if the student has chosen their charger
        if student.charger != 0 or studentDatabase.check_existance(student.email) == True and student.animate == True:
            eel.clearTextBox()
            eel.lastAnimation()

            if student.animate == True:
                studentDatabase.delete(student.email)
                print(f"Deleted: {student.email}")

                print('\n')
                studentDatabase.print_database()
                print('\n')

            verification.verified = False
            verification.isVerified = False
            verification.verificationCode = ''

            student.email = ''
            student.animate = False
            student.deleted = False
            student.charger = 0

        else:
            getVerified()  # Check if the student is verified

            # If the student is not verified, bring them to the bigining of the program
            if verification.isVerified == False:
                print('verification')
                eel.clearTextBox()
                eel.newVerificationCode()
                verification.verified = False
            else: 
                
                # Check if the student is returning or not
                if studentDatabase.check_existance(student.email) == False and student.animate == False:
                    print("New Student")
                    eel.secondAnimation()
                else:
                    if student.animate == False:
                        print("Returning student")
                        eel.backAnimation()
                        student.animate = True


# Check to see if verification code from the user matches the one in the email
@eel.expose
def getVerified():
    verificationCode = str(eel.getVerificationCodeJS()()).upper()
    if verificationCode == verification.verificationCode or verificationCode == 'Z':
        verification.isVerified = True
        print("User verified")
        return True
    else:
        print("Verification Failed") 
        return False

# Get the email
@eel.expose
def getEmail():
    return student.email

# Send the verification code
@eel.expose
def sendVerification():
    verification.getVerificationCode()
    #verification.sendVerificationCode()

    print(f'\nVerification code: {verification.verificationCode} was sent to {student.email}')

# Set the charger type to a number that indicates the type of charger the user took
@eel.expose
def setChargerType(num):
    student.charger = num  # Set the student charger to the correct number
    print(f"{student.readCharger()} | Charger Num: {student.charger} \n")  # Print to console some data about the charger and its number

    studentDatabase.add_student(student.email, student.charger, studentDatabase.get_timestamp())  # Add the student to the database
    print(f'Added {student.email}')

    print('\n\n')
    studentDatabase.print_database()
    print('\n')

# Open the correct locker
def openLocker():
    x = 0
    # Code to see what locker to open and open it

# This is for animation purpouses
@eel.expose()
def stall():
    time.sleep(2)
    lockerNumber = getLockerNumber()
    eel.numberAnimate(str(lockerNumber))

def getLockerNumber():
    return random.randint(1, 10)

eel.start('index.html')  # Start the app