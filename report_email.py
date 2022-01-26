#!/usr/bin/env python3

import os
from datetime import date
from reports import generate_report
import emails

attachment_path = '/tmp/processed.pdf'


def generate_email():
    attachment = '/tmp/processed.pdf'
    title = "Processed update on " + str(today)
    table_data = []
    for k, v in data.items():
        table_data.append([k, v])
        print(table_data)
    paragraph = "</n>".join(data)
    print(paragraph)
    reports.generate_report(title, paragraph)





if __name__ == "__main__":
    today = date.today()
    generate_email()
