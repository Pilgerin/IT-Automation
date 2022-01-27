#!/usr/bin/env python3
import os
import shutil
import psutil
import socket
from network import *
import emails


# checks disk space
def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20


# checks processor load
def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 80


# checks available memory
def check_memory_usage():
    memory = psutil.virtual_memory().available
    total = memory / 1024 ** 2  # multiplies to get memory in MBs
    return total > 500


# localhost = socket.gethostbyname('localhost')
def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == "127.0.0.1"

def create_warning_email(error):
    sender = 'automation@example.com'
    recipient = os.environ["USER"]
    subject = error
    body = "Please check your system and resolve the issue as soon as possible."
    err_msg = emails.generate(sender,recipient,subject,body)
    emails.send(err_msg)

# If there's not enough disk, or not enough CPU, print an error and send a scary email
if not check_disk_usage('/'):
    subject = "Error - Available disk space is less than 20%"
    create_warning_email(subject)
if not check_cpu_usage():
    subject = "Error - CPU usage is over 80%"
    create_warning_email(subject)
if not check_localhost():
    subject = 'Error - localhost cannot be resolved to 127.0.0.1'
    create_warning_email(subject)
if not check_memory_usage():
    subject = "Error - Available memory is less than 500MB"
    create_warning_email(subject)



