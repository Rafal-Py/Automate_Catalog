#!/usr/bin/env python3

import shutil
import psutil
import emails


sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
body = "Please check your system and resolve the issue as soon as possible."
message = None

#Check CPU usage
cpu_usage = psutil.cpu_percent(interval = 60)
if cpu_usage > 80%:
    subject = "Error - {}".format("CPU usage is over 80%")
    message = emails.generate_email(sender, recipient, subject, body)

#Check memory usage
mem = psutil.virtual_memory()
THRESHOLD = 500 * 1024 * 1024  # 500MB
if mem.available < THRESHOLD:
    subject = "Error - {}".format("Available memory is less than 500MB")
    message = emails.generate_email(sender, recipient, subject, body)

#Check disk space availability
dsk = shutil.disk_usage("/")
if dsk.free < dsk.total * 20%:
    subject = "Error - {}".format("Available disk space is less than 20%")
    message = emails.generate_email(sender, recipient, subject, body)

#Check if localhost is 127.0.0.1

if message is not None:
    emails.send_email(message)
