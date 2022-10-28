from app import mail
from os import getenv
from flask_mail import Message
from flask import render_template


class Mailing:
    def __init__(self):
        self.sender = (
            'No reply',
            getenv('MAIL_USERNAME')
        )

    def email_reset_password(self, recipient, password):
        html = render_template('reset_password.html', password=password)
        return self.__send_email(
            'password reset',
            [recipient],
            html
        )

    def __send_email(self, subject, recipients, message):
        message = Message(
            subject=subject,
            sender=self.sender,
            recipients=recipients,
            html=message
        )
        return mail.send(message)
