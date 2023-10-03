# from django import forms
from .models import Customer
# from django.contrib.auth.forms import UserCreationForm

# class CustomerRegistrationForm(UserCreationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control'}))
#     email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

# class CustomerProfileForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = ['name','locality','city','zipcode','state']
#         widgets = {
#             'name':forms.TextInput(attrs={'class':'form-control'}),
#            'locality':forms.TextInput(attrs={'class':'form-control'}),
#            'city':forms.TextInput(attrs={'class':'form-control'}),
#            'zipcode':forms.NumberInput(attrs={'class':'form-control'}),
#            'state':forms.Select(attrs={'class':'form-control'}),
#            'zipcode':forms.NumberInput(attrs={'class':'form-control'}),
#        }