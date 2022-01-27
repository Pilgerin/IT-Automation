#!/usr/bin/env python3

import os
import emails
from datetime import date
from reports import generate
from run import catalog_creation

today = date.today().strftime('%Y-%m-%d')


def generate_attachment(path):
    pdfdescr = ""
    for txtdescr in path:
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
    path_in = os.listdir('/supplier-data/descriptions')
    title = "Processed update on " + today
    attachment = generate('/tmp/processed.pdf', title,
                          generate_attachment(path_in))
    attachment_path = '/tmp/processed.pdf'
    # calling the report function from custom module
    email_subject = 'Upload Completed - Online Fruit Store'
    # subject line give in assignment for email
    email_body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'  # body line give in assignment for email
    msg = emails.generate("automation@example.com", "{}@example.com".format(user),
                          email_subject, email_body,
                          attachment_path)
    # structuring email and attaching the file. Then sending the email, using the cus$
    emails.send(msg)
