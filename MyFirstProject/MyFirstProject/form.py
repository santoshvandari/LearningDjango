from django import forms

class UserDataForm(forms.Form):
    name=forms.CharField(label="Name",required=False,)
    address=forms.CharField()
    msg=forms.CharField()