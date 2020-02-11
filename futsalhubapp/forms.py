from django import forms
from futsalhubapp.models import User,Player,Training


class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"


class PlayerForm(forms.ModelForm):
    class Meta:
        model=Player
        fields="__all__"


class TrainingForm(forms.ModelForm):
    class Meta:
        model=Training
        fields="__all__"