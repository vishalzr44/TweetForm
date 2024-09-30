"""import froms and tweet"""

from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

"""tweet form """
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['name','text', 'photo']

"""userRegistration form"""

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
