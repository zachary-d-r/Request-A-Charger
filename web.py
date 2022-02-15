import Student
import eel
import Verification
import time
import random
import Database

# Import the required functions for onefile mode
from os import chdir
import sys

# If the directory should be the onefile directory, then change the directory to the onefile directory
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    chdir(sys._MEIPASS)

student = Student.student()  # Create student object to store some info
verification = Verification.verification('', 'requestacharger@gmail.com', 'Kirby321%') #TODO remove('', 'requset-a-charger@computer4u.com', 'SC59UB8LY') # Create verification object to email the verification code 'requset-a-charger@computer4u.com'
studentDatabase = Database.StudentDatabase(r'Databases\studentData.dat')  # Create the student database
lockerDatabase = Database.LockerDatabase(r'Databases\lockerData.dat') # Create the locker database

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
        if student.charger != 0 or studentDatabase.check_existence(student.email) == True and student.animate == True:
            eel.clearTextBox()
            eel.lastAnimation()

            if student.animate == True:
                studentDatabase.remove_student(student.email)
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

            # If the student is not verified, bring them to the beginning of the program
            if verification.isVerified == False:
                print('verification')
                eel.clearTextBox()
                eel.newVerificationCode()
                verification.verified = False
            else: 
                
                # Check if the student is returning or not
                if studentDatabase.check_existence(student.email) == False and student.animate == False:
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
    verification.sendVerificationCode()

    print(f'\nVerification code: {verification.verificationCode} was sent to {student.email}')

# Set the charger type to a number that indicates the type of charger the user took
@eel.expose
def setChargerType(num):
    student.charger = num  # Set the student charger to the correct number
    print(f"{student.readCharger()} | Charger Num: {student.charger} \n")  # Print to console some data about the charger and its number

# Open the correct locker
def openLocker():
    x = 0
    # Code to see what locker to open and open it

# This is for animation purposes
@eel.expose()
def stall():
    time.sleep(2)
    lockerNumber = getLockerNumber()
    eel.numberAnimate(str(lockerNumber))

def getLockerNumber():
    if studentDatabase.check_existence(student.email) == False:
        print('Find locker for new student')
        print('ABC:', student.charger)

        studentDatabase.add_student(student.email, student.charger, studentDatabase.get_timestamp())  # Add the student to the database
        print(f'Added {student.email}')
        print('\n\n')
        studentDatabase.print_database()
        print('\n')
        
        return lockerDatabase.find_locker(student.charger)
    else:
        print('Find empty locker')
        student.charger = studentDatabase.get_student(student.email)["Charger Type"]
        return lockerDatabase.find_locker(student.charger, True)
        

eel.start('index.html', mode='chrome', cmdline_args=['--kiosk'])  # Start the app