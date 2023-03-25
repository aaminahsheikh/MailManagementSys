from . models import Customer, IncomingMail, OutgoingMail
from django.forms import ModelForm
from django import forms

class IncomingMailForm(ModelForm):
    class Meta:
        model = IncomingMail
        fields = '__all__'
        #exclude = ['customer']

    
class OutgoingMailForm(ModelForm):
    class Meta:
        model = OutgoingMail
        fields = '__all__'
        