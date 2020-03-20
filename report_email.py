#!/usr/bin/env python3

import os
from datetime import date
import reports
import json
import emails

def main():
    #Generate report in PDF
    attachment = "/tmp/processed.pdf"
    title = "Processed Update on {}".format(date.today())
    paragraph = ""

    with open('descriptions.json', 'r') as desc_json:
        descriptions = json.load(desc_json)

    for description in descriptions:
        paragraph += "name: {}\n".format(description["name"])
        paragraph += "weight: {} lbs\n".format(description["weight"])

    reports.generate_report(attachment, title, paragraph)

    #Generate the email
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, recipient, subject, body, attachment)

    #Send the email
    #emails.send_email(message)

if __name__ == "__main__":
    main()
