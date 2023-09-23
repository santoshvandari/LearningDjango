from django import forms

class UserDataForm(forms.Form):
    name=forms.TextInput()
    address=forms.TextInput()
    msg=forms.TextInput()