import email
import smtplib
import mimetypes
import os


def generate_email(sender, recipient, subject, body, attachment):
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    if not attachment == "":
        attachment_filename = os.path.basename(attachment)
        mimetype = mimetypes.guess_type(attachment)
        # add attachment



def send_email(message):
    """Sends the message to the configured SMTP server."""
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()


if __name__ == "__main__":
    pass
