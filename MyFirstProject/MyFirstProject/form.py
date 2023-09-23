from django import forms

class UserDataForm(forms.Form):
    name=forms.TextInput(label="Name")
    address=forms.TextInput(label="Address")
    msg=forms.TextInput(label="Message")