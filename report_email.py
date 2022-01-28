#!/usr/bin/env python3

import os
import emails
from datetime import date
import reports

today = date.today().strftime('%Y-%m-%d')


def generate_attachment(path):
    files = os.listdir(path)
    pdfdescr = ""
    for txtdescr in files:
        # traverses each file in the directory
        if txtdescr.endswith('.txt'):
            with open(path + txtdescr, 'r') as infile:
                description = infile.readlines()
                name = description[0].strip()
                weight = description[1].strip()
                pdfdescr += "Name: " + name + "\n" + "Weight: " + weight + "\n"
    return pdfdescr


if __name__ == "__main__":
    user = os.environ["USER"]
    path = 'supplier-data/descriptions/'
    title = "Processed update on " + today
    attachment = generate_attachment(path)
    reports.generate("/tmp/processed.pdf", title, attachment)
    # calling the report function from custom module
    email_subject = 'Upload Completed - Online Fruit Store'
    # subject line give in assignment for email
    email_body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'  # body line give in assignment for email
    attachment_path = '/tmp/processed.pdf'
    msg = emails.generate("automation@example.com", "{}@example.com".format(user),
                          email_subject, email_body,
                          attachment_path)
    emails.send(msg)
