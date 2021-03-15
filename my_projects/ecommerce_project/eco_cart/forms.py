from django import forms

class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=120)
    last_name = forms.CharField(max_length=120)
    email = forms.CharField(max_length=120)
    address = forms.CharField(max_length=120)
    zipcode = forms.CharField(max_length=120)
    place = forms.CharField(max_length=120)
    stripe_token = forms.CharField(max_length=520)


