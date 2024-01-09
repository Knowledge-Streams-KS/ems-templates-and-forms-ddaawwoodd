from django import forms
# from .models import Event, Registration


class EventForm(forms.ModelForm):

    title = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    date = forms.DateTimeField()
    location = forms.CharField(max_length=200)


class RegistrationForm(forms.ModelForm):

    name = forms.CharField(max_length=200)
    email = forms.EmailField()