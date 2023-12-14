import socket
import schedule
import time
import smtplib

def get_ip():
    # Get hostname and ip address
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    # Send email with obtained IP address
    send_email(ip_address)
    
def send_email(ip_address):
    # Setting up email variables
    from_email = 'sender@example.com'  # Your email address
    to_email = 'recipient@example.com'  # Recipient's email address
    my_password = 'password'  # Password for the sender's email account
    smtp_server = 'smtp.example.com'  # SMTP server details (e.g., 'smtp.gmail.com' for Gmail)
    smtp_port = 587  # SMTP port number (587 for TLS, 465 for SSL)

    # Connecting to SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Initiating TLS connection
    server.login(from_email, my_password)  # Logging into the sender's email account
    
    # Composing email message
    message = f"The IP address for the Acta Verba Machine is {ip_address}"
    
    # Sending email and quitting the SMTP server connection
    server.sendmail(from_email, to_email, message)
    server.quit()

# Schedule to run 'get_ip' function every day at 09:00
schedule.every().day.at("09:00").do(get_ip)

# Infinite loop to continuously check and execute scheduled tasks
while True:
    schedule.run_pending()  # Check if any scheduled tasks are pending
    time.sleep(1)  # Sleep to avoid excessive CPU usage during the loop
