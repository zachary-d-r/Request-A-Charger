from email.mime.text import MIMEText
import smtplib
import random

class verification:
    
    codeNums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'F', 'L', 'Y', 'E', 'P', 'O', 'U', 'W', 'R', 'G', 'S', 'V', 'Z']  # Characters that can be in a verification code
    verificationCode = ''  # The code
    toAddress = ''  # Who we are sending the email to
    fromAddress = ''  # Who is sending the email

    # Initialize the object by setting the correct email addresses
    def __init__(self, to, fromEmail):
        self.toAddress = to
        self.fromAddress = fromEmail

    # Generate a random verification code
    def getVerificationCode(self):
        self.verificationCode = ''  # Reset the verification code

        # Add a random character from the list of characters above
        for i in range(9):
            self.verificationCode += self.codeNums[random.randint(0, len(self.codeNums)-1)]

    # Email the verification code to the client
    def sendVerificationCode(self):
        x = 0
