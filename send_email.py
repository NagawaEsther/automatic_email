import smtplib
from email.mime.text import MIMEText

# Your email credentials
smtp_server = 'smtp.gmail.com'
smtp_port = 587
your_email = 'nagawaesther227@gmail.com'
your_password = 'kqxmrupaxjndxagy'  # Use your Google App Password here

# Email content
to_email = 'dantetrevordrex@gmail.com'
subject = 'Test Email from Python SMTP script'
body = 'Hello, this is a test email to prove my script works.'

# Create message
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = your_email
msg['To'] = to_email

# Send email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(your_email, your_password)
    server.sendmail(your_email, to_email, msg.as_string())
    server.quit()
    print('Email sent successfully!')
except Exception as e:
    print(f'Failed to send email: {e}')
