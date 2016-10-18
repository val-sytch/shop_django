from django import forms


class OrderForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    phone = forms.CharField()
    email = forms.EmailField()