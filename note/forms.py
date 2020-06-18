from django import forms
from .models import Note


class EntryForm(forms.ModelForm):

    class Meta:
        model   = Note
        fields  = ('title', 'category', 'content')
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Title'
            }
        ),
            'category': forms.TextInput(attrs={
                    'placeholder': ''
                }
            ),
            'content': forms.Textarea(attrs={
                'placeholder': "Type a note"
            }
        ),
    }