from django import forms

class LoginForm(forms.Form):
    login_var = forms.CharField(label='Username or Email',required=False, max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(required=False,widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class SignupForm(forms.Form):

    username = forms.CharField(required=False,max_length=50)
    email = forms.EmailField(required=False,max_length=50)
    password = forms.CharField(required=False,widget=forms.PasswordInput())
    passwordConfirm = forms.CharField(required=False,widget=forms.PasswordInput())