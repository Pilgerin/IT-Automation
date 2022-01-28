#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib


def generate(sender, recipient, subject, body, attachment_path = None):
    """Creates an email with an attachment."""
    # Basic Email formatting
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    # attachment needs to be optional to take care of health check email without attachment
    if attachment_path is not None:
        # Process the attachment and add it to the email
        attachment_filename = os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/', 1)

        with open(attachment_path, 'rb') as fp:
            message.add_attachment(fp.read(),
                                   maintype=mime_type,
                                   subtype=mime_subtype,
                                   filename=attachment_filename)

    return message


def send(message):
    """Sends the message to the configured SMTP server."""
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
