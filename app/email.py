# from flask_mail import Message
# from flask import render_template
# from . import mail

# def mail_message(subject,template,to,**kwargs):
#     sender_email = 'owinolawrence21@gmail.com'
#     subject_pref = 'Pitches'
#     email = Message(subject, sender=sender_email, recipients=[to])
#     email.body= render_template(template + ".txt",**kwargs)
#     email.html = render_template(template + ".html",**kwargs)
#     mail.send(email)

from flask_mail import Message
from flask import render_template
from . import mail

def mail_message(subject,template,to,**kwargs):
    sender_email = 'bironodhiambo00@gmail.com.com'

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)