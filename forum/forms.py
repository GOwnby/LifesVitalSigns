from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(label='Email',  max_length=100, widget=forms.EmailInput)
    password = forms.CharField(label='Password', max_length=32, widget=forms.PasswordInput)

class AccountForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    email = forms.CharField(label='Email',  max_length=100, widget=forms.EmailInput)
    password = forms.CharField(label='Password', max_length=32, widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Password', max_length=32, widget=forms.PasswordInput)

class TopicForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    text = forms.CharField(label="Text", max_length=25000)