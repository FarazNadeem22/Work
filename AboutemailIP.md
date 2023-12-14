# Scheduled IP Address Email Notifier

This Python script is designed to fetch the local machine's IP address and send it via email to a specified recipient every day at a set time. It uses the `socket`, `schedule`, `time`, and `smtplib` modules for IP address retrieval, scheduling, timing, and email functionality.

## Functionality:

### `get_ip()` Function:
- Retrieves the local machine's hostname and IP address using the `socket` module.
- Invokes the `send_email(ip_address)` function to send an email with the obtained IP address.

### `send_email(ip_address)` Function:
- Sets up email-related variables such as sender's email, recipient's email, password, SMTP server, and port.
- Establishes a connection with the SMTP server using `smtplib`, starts a TLS session, and logs in with the sender's credentials.
- Creates an email message containing the IP address information and sends it to the recipient.
- Closes the SMTP server connection.

### Scheduling:
- Schedules the `get_ip` function to run daily at 09:00 using the `schedule` module.
- Runs an infinite loop to continuously check for scheduled tasks and execute them.
- Includes a sleep function to prevent excessive CPU usage within the loop.

### Instructions for Use:
1. Replace `'sender@example.com'`, `'recipient@example.com'`, `'password'`, and `'smtp.example.com'` in the script with your actual email credentials and SMTP server details.
2. Execute the script to initiate the scheduled email notifications.

This script is useful for automatically notifying designated recipients about changes in the machine's IP address on a daily basis.
