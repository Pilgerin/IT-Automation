#!/usr/bin/env python3

import os
from datetime import date
import reports

attachment_path = '/tmp/processed.pdf'

def load_data(filename):
    """Loads the contents of filename as a JSON file."""
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def generate_report(filename):
    table_data = [["name", "weight"]]
    for item in data:
        table_data.append([item["name"], (item["weight"])])
    report_table = Table(data=table_data)
    return report_table


if __name__ == "__main__":
    data = load_data('report.txt')
    summary = process_data(data)
    paragraph = "<br/>".join(summary)
    print(summary)
    reports.generate("processed.pdf", "Car report", paragraph, cars_dict_to_table(data))

def generate_report():

        data = "report.txt"
        filename = "processed.pdf"
        attachment = '/tmp/processed.pdf'
        title = "Processed update on " + str(today)
        table_data = []
        for k, v in data.items():
            table_data.append([k, v])
            print(table_data)
        paragraph = "</n>".join(data)
        print(paragraph)
        reports.generate_report(title, paragraph)

def send(message):
    """Sends the message to the configured SMTP server."""
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()


if __name__ == "__main__":
    today = date.today()

    generate_report()
