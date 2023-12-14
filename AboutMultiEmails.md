# Email IP Address Notifier

The "Email IP Address Notifier" is a Python script designed to retrieve the IP address of the local machine and send an email notification containing this information to specified recipients via a designated SMTP server. The script is structured into two main functions, `get_ip()` and `send_email(ip_address)`, along with auxiliary functionalities.

## Functionality:

### `get_ip()` Function:
- Retrieves the local machine's hostname and IP address using Python's `socket` module.
- Invokes the `send_email(ip_address)` function to compose and send an email with the fetched IP address.

### `send_email(ip_address)` Function:
- Sets up necessary variables like the sender's email address, recipient's email addresses, SMTP server details, and message content.
- Constructs an email message using `email.mime` modules to include the IP address and local time in the email body.
- Attempts to connect to the SMTP server using `smtplib` and sends the composed email to the specified recipients.
- Handles exceptions, printing error messages if there are any issues during email sending.

### Driver Code:
- Calls the `get_ip()` function to initiate the process of fetching the local machine's IP address and sending the email.

## Usage:
- The user needs to provide their own email address, recipient email addresses, and SMTP server details for proper functionality.
- The script can be scheduled to run periodically to notify recipients of any changes in the machine's IP address.

## Instructions for Use:
1. Modify the `from_email`, `recipients`, and `smtp_server` variables to match your email address, recipient email addresses, and SMTP server details.
2. Run the script to execute the functionality.

This script proves useful in scenarios where users need to monitor and notify changes in their machine's IP address to designated recipients via email.
