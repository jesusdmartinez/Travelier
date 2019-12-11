import smtplib
import secrets
import os

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(secrets.EMAIL_ADDRESS, secrets.PASSWORD)

    subject = "Grab dinner this weekend"
    body = "How about dinner at 6pm this saturday?"


    msg = f'Subject: {subject}\n\n{body}'

    smpt.sendmail(secrets.EMAIL_ADDRESS, secrets.EMAIL_ADDRESS, msg)




# def send_email(subject, msg):
#     try:
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.ehlo()
#         server.starttls()
#         server.login(secrets.EMAIL_ADDRESS, secrets.PASSWORD)
#         message = 'Subject: {}\n\n{}'.format(subject, msg)
#         server.sendmail(secrets.EMAIL_ADDRESS, secrets.EMAIL_ADDRESS, message)
#         server.quit()
#         print("Success, email sent")
#     except:
#         print("Email failed to send")
#
# Subject = "Test"
# msg = "Hello"
#
# send_email(Subject, msg)