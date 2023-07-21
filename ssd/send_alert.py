#-*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SENDER_EMAIL = 'huixintang963@gmail.com'
SENDER_PASSWORD = 'cyalgdpupqvryeko'
# RECEIVER_EMAIL = 's1110158@my.cmsh.cyc.edu.tw'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SUBJECT = 'Alert!'

def send_email(message):

    # get receiver email
    receiver_email = input("Please enter the recipient's email address :")
    
    # create email content
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = receiver_email
    msg['Subject'] = SUBJECT

    # Add email message
    msg.attach(MIMEText(message, 'plain'))

    try:
        # log into SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)

        # send email
        server.sendmail(SENDER_EMAIL, receiver_email, msg.as_string())
        print('Mail sent successfully')

        # close connection
        server.quit()
    except Exception as e:
        print('Email sending failed:', str(e))