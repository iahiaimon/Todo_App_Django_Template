from django import forms
from .models import CustomUser , Todo

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = "__all__"

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"