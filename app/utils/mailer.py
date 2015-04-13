from app.decorators import async
from flask_mail import Message
from flask import render_template
from app import app
from config import MAIL_USERNAME

__author__ = 'erik'
from app import mail
message_sender = MAIL_USERNAME

@async
def send_async_email(msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, recipients, text_body, html_body):
    msg = Message(subject, sender=("Me", message_sender), recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    send_async_email(msg)


def send_confirm_email(email_conf, user):
    with app.app_context():
        confirm_html = render_template("confirm_email_tmp.html", mail_data=email_conf)
        text_body = "text "
        subject = "Confirmation link"
        send_email(subject, [user.email], text_body, confirm_html)