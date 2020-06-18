from django import forms
from .models import Note


class NoteForm(forms.ModelForm):

    class Meta:
        model   = Note
        fields  = ('title', 'category', 'content')
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Title'
            }
        ),
            'category': forms.TextInput(attrs={
                    'placeholder': 'Identify a Category: '
                }
            ),
            'content': forms.Textarea(attrs={
                'placeholder': "Type a note"
            }
        ),
    }