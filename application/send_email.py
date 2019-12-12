import smtplib
import secrets
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = "Your Trip to Brazil from The Travelier"
msg['From'] = secrets.EMAIL_ADDRESS
msg['To'] = secrets.EMAIL_ADDRESS
msg.set_content('Hi Jesus\n\nThank you for messsaging the Travlier.  We have put togther some ideas for your trip, please see here\nhttps://wetu.com/Itinerary/Landing/fbd37720-bfa2-4f05-8827-a9b0f8b46bf1')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(secrets.EMAIL_ADDRESS, secrets.PASSWORD)

    smtp.send_message(msg)