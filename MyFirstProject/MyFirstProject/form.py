from django import forms

class UserDataForm(forms.Form):
    Name=forms.TextInput(label="Name")
    add=forms.TextInput(label="Address")
    msg=forms.TextInput(label="Message")