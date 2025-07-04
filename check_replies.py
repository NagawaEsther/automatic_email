import imaplib
import email
from email.header import decode_header

# Your email credentials
your_email = "nagawaesther227@gmail.com"
your_password = "kqxmrupaxjndxagy"  # Your app password (no spaces)

# Connect to Gmail IMAP server
imap_server = "imap.gmail.com"
mail = imaplib.IMAP4_SSL(imap_server)

# Login
mail.login(your_email, your_password)

# Select the inbox
mail.select("inbox")

# Search for unread messages FROM your lecturer
status, messages = mail.search(None, '(UNSEEN FROM "dantetrevordrex@gmail.com")')

# Get list of email IDs
email_ids = messages[0].split()

if not email_ids:
    print("❌ No new replies from your lecturer yet.")
else:
    for email_id in email_ids:
        # Fetch the email
        res, msg_data = mail.fetch(email_id, "(RFC822)")
        raw_email = msg_data[0][1]

        # Parse the email content
        msg = email.message_from_bytes(raw_email)

        # Decode subject
        subject = decode_header(msg["Subject"])[0][0]
        if isinstance(subject, bytes):
            subject = subject.decode()

        from_ = msg.get("From")

        print(f"\n✅ New email from: {from_}")
        print(f"Subject: {subject}")

        # Get the email body
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                if content_type == "text/plain":
                    body = part.get_payload(decode=True).decode()
                    print(f"\n📩 Message body:\n{body}")
                    break
        else:
            body = msg.get_payload(decode=True).decode()
            print(f"\n📩 Message body:\n{body}")

# Logout
mail.logout()
