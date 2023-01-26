import socket
import schedule
import time
import smtplib


def get_ip():

    # Get hostname and ip address
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    # Send email
    send_email(ip_address)
    
def send_email(ip_address):
    
    # Setting up variables
    from_email = 'acta.Verba@mail.com'
    to_email = 'afinit.psg@afiniti.com'
    my_password = 'passworD'
    smtp_server = 'smtp.afiniti.com'

    # Connecting to Server
    server = smtplib.SMTP(smtp_server, 507)
    server.starttls()
    server.login(from_email, my_password)

    # Create message 
    message = f"The IP address for the Acta Verba Machine is {ip_address}"

    # Send email and quit()
    server.sendmail(from_email,to_email, message)
    server.quit()

schedule.every().day.at("09:00").do(get_ip)

while True:
    schedule.run_pending()
    time.sleep(1)
