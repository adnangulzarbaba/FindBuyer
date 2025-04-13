import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set your credentials here
EMAIL_ADDRESS = 'example@gmail.com'
EMAIL_PASSWORD = 'qwerty@123'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587


def send_emails(results, material):
    success = True  # track if all emails are successful

    for entry in results:
        if entry['email'] == 'N/A':
            continue

        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = entry['email']
        msg['Subject'] = "Potential Collaboration Opportunity"

        body = f"""
        Hello,

        We noticed that your product, '{entry['product']}',
        incorporates {material}.

        Our company specializes in supplying high-quality {material},
        and we’d love the opportunity
        to explore a potential collaboration with you.

        Looking forward to connecting!

        Best regards,
        The Supplier Team
        """
        msg.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.send_message(msg)
                print(f"✅ Email sent to {entry['email']}")
        except Exception as e:
            print(f"❌ Failed to send email to {entry['email']}: {e}")
            success = False  # even one failure marks overall failure

    return success
