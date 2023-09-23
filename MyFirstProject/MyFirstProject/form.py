from django import forms

class UserDataForm(forms.Form):
    name=forms.CharField(label="Name",required=False, widget=forms.TextInput)
    address=forms.CharField(label="Address",required=False, widget=forms.TextInput)
    msg=forms.CharField(label="Message",required=False,widget=forms.Textarea)