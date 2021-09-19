#Send an email with python
#Friday Sep 17, 2021
#Ethan Present

#The sender has to have an outlook domain. A gmail domain won't work because of google security features


#importing the libraries
import smtplib, ssl
from email.message import EmailMessage, Message



#constents for message and subject of email
MESSAGE = """
This is where your
message goes"""
SUBJECT = 'This is your Subject'

SENDER_EMAIL_ADDRESS = ''
RECEIVER_EMAIL_ADDRESS = ''
PASSWORD = ''

#function for sending email, reqires: message and subject of email, along with email information such as sender, receiver, and password of sender
def SendEmail(MESSAGE, SUBJECT, senderEmail, ReceiverEmail, password=None):
    #if the user did not want to enter the password in the function parameters then they can enter it as user input
    if password == None:
        password = input('Please enter your password\n')

    #setting up an email message
    msg = EmailMessage()
    msg.set_content(MESSAGE) #Message of email

    #Subject, from, and to (information for email)
    msg['Subject'] = SUBJECT
    msg['From'] = senderEmail
    msg['To'] = ReceiverEmail

        
    server = smtplib.SMTP('smtp-mail.outlook.com', 587) #logging into an outlook server (this is only for the sender. Meaning the sender has to be outlook. You can send an email to any domain)
    server.starttls()
    server.login(senderEmail, password) #login to the email
    print('login successful')
    server.send_message(msg) #send message
    print('email has been sent to ', ReceiverEmail)
    server.quit() #quitting the sever
    print('server quitting')

SendEmail(MESSAGE, SUBJECT, SENDER_EMAIL_ADDRESS, RECEIVER_EMAIL_ADDRESS, password=PASSWORD)
