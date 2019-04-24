from django import forms
from .models import Message#, CustomUser
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class MsgForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('from_user', 'to_user', 'subject', 'body', 'timestamp', 'read_status', 'received_trash_status', 'sent_trash_status')

        labels = {
            'from_user': (''),
            'to_user': ('To'),
            'subject': ('Subject'),
            'body': (''),
            'timestamp': (''),
            'read_status': (''),
            'received_trash_status': (''),
            'sent_trash_status': ('')
            

        }
