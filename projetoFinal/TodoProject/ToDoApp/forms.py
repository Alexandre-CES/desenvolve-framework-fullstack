from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm

class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ['title', 'description', 'completed']
    widgets = {
      'title': forms.TextInput(attrs={'class':'form-control'}),
      'description': forms.Textarea(attrs={'class': 'form-control'}),
      'completed': forms.CheckboxInput(attrs={'class':'form-check-input'})
    }


class BootstrapUserCreationForm(UserCreationForm):
  class Meta(UserCreationForm.Meta):
    fields = ['username', 'password1', 'password2']
    widgets = {
      'username': forms.TextInput(attrs={'class': 'form-control'}),
      'password1': forms.PasswordInput(attrs={'class':'form-control'}),
      'password2': forms.PasswordInput(attrs={'class':'form-control'})
    }