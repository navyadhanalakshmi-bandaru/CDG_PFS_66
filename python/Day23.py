# ============================================================
# Day 23: Email Automation
# ============================================================
# SubTopics:
# 1. Sending Emails using Python
# 2. Subject & Attachments
# 3. Bulk Mail Sending
#
# Note:
# Never write your real email password directly in this file.
# Use an App Password or environment variable.
# ============================================================


# ============================================================
# IMPORTS
# ============================================================

import smtplib
from email.message import EmailMessage


# ============================================================
# EMAIL CONFIGURATION
# ============================================================

# Example for Gmail:
# SMTP server = smtp.gmail.com
# SMTP port   = 587
#
# Replace these with your own test email and App Password.

SENDER_EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password"

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587


# ============================================================
# 1. SENDING EMAILS USING PYTHON
# ============================================================

def send_email(receiver_email, subject, message):

    email = EmailMessage()

    email["From"] = SENDER_EMAIL
    email["To"] = receiver_email
    email["Subject"] = subject

    email.set_content(message)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:

        server.starttls()

        server.login(SENDER_EMAIL, APP_PASSWORD)

        server.send_message(email)

    print("Email sent successfully!")


# Example:
#
# send_email(
#     "receiver@gmail.com",
#     "Python Email Test",
#     "Hello! This email was sent using Python."
# )


# ============================================================
# 2. SUBJECT & ATTACHMENTS
# ============================================================

def send_email_with_attachment(
    receiver_email,
    subject,
    message,
    file_path
):

    email = EmailMessage()

    email["From"] = SENDER_EMAIL
    email["To"] = receiver_email
    email["Subject"] = subject

    email.set_content(message)


    # Open the attachment

    with open(file_path, "rb") as file:

        file_data = file.read()

        file_name = file.name.split("/")[-1]

        email.add_attachment(
            file_data,
            maintype="application",
            subtype="octet-stream",
            filename=file_name
        )


    # Connect to email server

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:

        server.starttls()

        server.login(SENDER_EMAIL, APP_PASSWORD)

        server.send_message(email)

    print("Email with attachment sent successfully!")


# Example:
#
# send_email_with_attachment(
#     "receiver@gmail.com",
#     "Python File",
#     "Please find the attached file.",
#     "sample.txt"
# )


# ============================================================
# 3. BULK MAIL SENDING
# ============================================================

def send_bulk_email(receivers, subject, message):

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:

        server.starttls()

        server.login(SENDER_EMAIL, APP_PASSWORD)


        for receiver in receivers:

            email = EmailMessage()

            email["From"] = SENDER_EMAIL
            email["To"] = receiver
            email["Subject"] = subject

            email.set_content(message)

            server.send_message(email)

            print("Email sent to:", receiver)


# Example:
#
# receivers = [
#     "test1@gmail.com",
#     "test2@gmail.com",
#     "test3@gmail.com"
# ]
#
# send_bulk_email(
#     receivers,
#     "Python Practice",
#     "Hello! This is a Python automation test email."
# )


# ============================================================
# BULK EMAIL WITH ATTACHMENT
# ============================================================

def send_bulk_email_with_attachment(
    receivers,
    subject,
    message,
    file_path
):

    with open(file_path, "rb") as file:

        file_data = file.read()

        file_name = file.name.split("/")[-1]


    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:

        server.starttls()

        server.login(SENDER_EMAIL, APP_PASSWORD)


        for receiver in receivers:

            email = EmailMessage()

            email["From"] = SENDER_EMAIL
            email["To"] = receiver
            email["Subject"] = subject

            email.set_content(message)

            email.add_attachment(
                file_data,
                maintype="application",
                subtype="octet-stream",
                filename=file_name
            )

            server.send_message(email)

            print("Email sent to:", receiver)


# Example:
#
# receivers = [
#     "test1@gmail.com",
#     "test2@gmail.com"
# ]
#
# send_bulk_email_with_attachment(
#     receivers,
#     "Python Assignment",
#     "Please find the assignment attached.",
#     "assignment.pdf"
# )


# ============================================================
# PRACTICE: EMAIL USING USER INPUT
# ============================================================

def create_email():

    receiver = input("Enter receiver email: ")

    subject = input("Enter subject: ")

    message = input("Enter message: ")

    return receiver, subject, message


# Example:
#
# receiver, subject, message = create_email()
#
# send_email(
#     receiver,
#     subject,
#     message
# )


# ============================================================
# PRACTICE: PERSONALIZED BULK EMAIL
# ============================================================

def send_personalized_emails(student_emails):

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:

        server.starttls()

        server.login(SENDER_EMAIL, APP_PASSWORD)


        for name, email_address in student_emails:

            email = EmailMessage()

            email["From"] = SENDER_EMAIL
            email["To"] = email_address

            email["Subject"] = "Python Course Update"

            message = f"""
Hello {name},

This is a Python email automation practice message.

Regards,
Python Team
"""

            email.set_content(message)

            server.send_message(email)

            print("Email sent to:", name)


# Example:
#
# students = [
#     ("Navya", "test1@gmail.com"),
#     ("Rahul", "test2@gmail.com")
# ]
#
# send_personalized_emails(students)


# ============================================================
# IMPORTANT NOTES
# ============================================================

# 1. Never share your email password or App Password.
#
# 2. Do not put real passwords directly in GitHub code.
#
# 3. For real projects, use environment variables.
#
# 4. Send bulk emails only to recipients who expect them.
#
# 5. Use small test recipient lists while learning.


# ============================================================
# END OF DAY 23
# ============================================================