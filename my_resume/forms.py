from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model= Message
        fields=['name','email', 'message']

        widgets={
                'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your name'}),
                'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Your Email address'}),
                'message':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Your Message'}),
        }