from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from posts.models import Post


class UserModelForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Username or Password is invalid!!!")

        return self.cleaned_data


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ["author", "slug"]





