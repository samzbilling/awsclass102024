import boto3

ses = boto3.client('ses')

def verify_ses_email(email):
    """Verify an email address in SES."""
    try:
        ses.verify_email_identity(EmailAddress=email)
        print(f"Verification email sent to '{email}'. Please verify it in your inbox.")
    except Exception as e:
        print(f"Error verifying email '{email}': {e}")

def send_ses_email(sender, recipient, subject, body):
    """Send an email report via SES."""
    try:
        ses.send_email(
            Source=sender,
            Destination={"ToAddresses": [recipient]},
            Message={
                "Subject": {"Data": subject},
                "Body": {"Text": {"Data": body}}
            }
        )
        print(f"Email sent to '{recipient}' with subject '{subject}'.")
    except Exception as e:
        print(f"Error sending email: {e}")
