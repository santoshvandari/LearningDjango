#Welcome Email
from SignInSignUp import settings as setting

senderemail=setting.EMAIL_HOST_USER
receiveremail=setting.EMAIL_HOST_USER
class WelcomeMessage:
    def __init__(self,fullname):
        self.username=fullname
    subject = "Welcome to Website - Django Login!!!"
    message="Hello {full},\n\nWelcome to Django Login.\n\n Please Activate account by Confirming it.\n\nThanks,\nDjango Login Team"

    def SendEmail():
        pass