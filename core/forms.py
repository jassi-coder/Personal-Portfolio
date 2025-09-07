# forms.py
from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'id': 'name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email', 'id': 'email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message', 'id': 'message'}),
        }
