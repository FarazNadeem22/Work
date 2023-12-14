import socket
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_ip():
    # Get hostname and ip address
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    # Send email
    send_email(ip_address)


def send_email(ip_address):
    # Setting up variables
    from_email = 'maf22@gmail.com'  # Replace 'Your email' with your email address
    recipients = ['recipient1@example.com', 'recipient2@example.com']  # Add recipient email addresses
    smtp_server = '198.233.3.180'  # Replace 'smtp Server' with your SMTP server IP address or domain
    current_time = datetime.now().strftime("%H:%M:%S")
    smtp_port = 25

    # Construct email
    message = MIMEMultipart()
    message_text = f"This is a test\n The current ip address is: {ip_address}\nLocal time: {current_time}"
    message["Subject"] = f"The current ip address is: {ip_address}"
    message["From"] = from_email
    message["To"] = ", ".join(recipients)
    message.attach(MIMEText(message_text))

    # Connecting to Server
    server = smtplib.SMTP(smtp_server, smtp_port)
    try:
        # Send email and quit()
        server.sendmail(from_email, recipients, message.as_string())
        print("Email sent")
        server.quit()
    except Exception as e:
        print("Something went wrong:", e)
        server.quit()


'''Driver'''
get_ip()
