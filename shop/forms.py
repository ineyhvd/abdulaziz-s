from tables import Comment

from django import forms
from phonenumber_field.modelfields import PhoneNumberField


class OrderForm(forms.Form):
    full_name = forms.CharField()
    phone_number = PhoneNumberField(region='UZ')
    quantity = forms.IntegerField()


class CommentForm(forms.ModelForm):
    full_name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
