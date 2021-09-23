import smtplib, ssl
from email.message import EmailMessage, Message
import random


class verification:
    
    MESSAGE = ''  # This is your message
    SUBJECT = ''  # This is your subject

    SENDER_EMAIL_ADDRESS = ''
    RECEIVER_EMAIL_ADDRESS = ''
    PASSWORD = ''

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
        # If the user did not want to enter the password in the function parameters then they can enter it as user input
        if self.password == None:
            password = input('Please enter your password\n')

        # Setting up an email message
        msg = EmailMessage()
        msg.set_content(self.MESSAGE) #Message of email

        # Subject, from, and to (information for email)
        msg['Subject'] = self.SUBJECT
        msg['From'] = self.senderEmail
        msg['To'] = self.ReceiverEmail

            
        server = smtplib.SMTP('smtp-mail.outlook.com', 587) # Logging into an outlook server (this is only for the sender. Meaning the sender has to be outlook. You can send an email to any domain)
        server.starttls()
        server.login(self.senderEmail, password) # Login to the email
        print('login successful')
        server.send_message(msg) # Send message
        print('email has been sent to ', self.ReceiverEmail)
        server.quit() # Quitting the sever
        print('server quitting')
