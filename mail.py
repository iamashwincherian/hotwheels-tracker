from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os

from config import URL

load_dotenv()

SEND_EMAIL = eval(os.getenv('SEND_EMAIL'))
EMAIL_ID = os.getenv('EMAIL_ID')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')


def send_email(new_drops):
    if not SEND_EMAIL:
        return

    def make_body():
        body = f'<h3>Here is the list of new hot wheel drops in <a href="{
            URL}">Karzanddolls</a>:</h3>'
        table = '<table border="1" style="border: 1px solid black; border-collapse: collapse; border-spacing: 0px;">'
        for drop in new_drops:
            table += f'<tr><td style="padding: 5px 10px;">{drop}</td></tr>'
        table += '</table>'
        body += table
        return body

    message = MIMEMultipart()
    message['From'] = f'Hot Wheels Tracker <{EMAIL_ID}>'
    message['To'] = EMAIL_ID
    message['Subject'] = 'New Hotwheels Drop!'
    message.attach(MIMEText(make_body(), 'html'))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ID, EMAIL_PASSWORD)
        server.sendmail(message['From'], message['To'], message.as_string())
        server.quit()
        print("Email Sent!")
    except Exception as e:
        print(f"Error: {str(e)}")
