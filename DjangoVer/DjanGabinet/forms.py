from django.forms import ModelForm
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models import User
from django     import forms
from .models    import Users2

class RegisterForm(ModelForm):
    class Meta:
        model = Users2
        fields = '__all__'
