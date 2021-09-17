from email.mime.text import MIMEText
import smtplib
import random

class verification:
    
    codeNums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'F', 'L', 'Y', 'E', 'P', 'O', 'U', 'W', 'R', 'G', 'S', 'V', 'Z']
    verification = ''
    toAddress = ''
    fromAddress = ''

    def __init__(self, to, fromEmail):
        self.toAddress = to
        self.fromAddress = fromEmail

    def getVerificationCode(self):
        self.verification = ''
        for i in range(9):
            self.verification += self.codeNums[random.randint(0, len(self.codeNums)-1)]

    def sendVerificationCode(self):
        x = 0
