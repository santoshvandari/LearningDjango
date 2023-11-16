#Welcome Email
from SignInSignUp import settings as setting
from django.core.mail import send_mail

senderemail=setting.EMAIL_HOST_USER
class WelcomeMessage:
    def __init__(self,fullname,receiveremail):
        self.username=fullname
        self.receiveremail=receiveremail
    subject = "Welcome to Website - Django Login!!!"
    message="Hello {full},\n\nWelcome to Django Login.\n\n Please Activate account by Confirming it.\n\nThanks,\nDjango Login Team"

    def SendEmail(self):
        send_mail(self.subject,self.message,senderemail,self.receiveremail,fail_silently=False)