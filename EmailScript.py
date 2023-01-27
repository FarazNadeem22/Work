import socket
from datetime import datetime
import time
import smtplib
from email.mime.text import MIMEText


def get_ip():
    # Get hostname and ip address
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    # Send email
    send_email(ip_address)
    
def send_email(ip_address):
    # Setting up variables
    from_email = 'myemail'
    to_email = 'youremail'
    smtp_server = 'SMTP Server'
    current_time = datetime.now().strftime("%H:%M:%S")

    # Connecting to Server
    server = smtplib.SMTP(smtp_server, 25)


    # Create message 
    message = MIMEText(f"The IP address for the Acta Non Verba Machine is {ip_address}")
    message["subject"] =  f"[DECFON 5] - [Acta non Verba] - [The current ip address is: {ip_address}] [{current_time}]"
    message["FROM"] = from_email
    message["To"] = to_email 
    
    try:
        # Send email and quit()
        server.sendmail(from_email,to_email, message.as_string())
        print("Email sent")
        server.quit()
    except:
        print("Something went wrong")
        server.quit()
        
"""Driver"""
get_ip()
