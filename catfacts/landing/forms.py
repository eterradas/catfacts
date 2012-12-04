from django import forms
from django.contrib.localflavor.us.forms import USPhoneNumberField
from landing.models import Recipient

class RecipientForm(forms.Form):
    number = USPhoneNumberField(label='Your number', widget=forms.TextInput(attrs={'placeholder': '510-555-5555', 'class':'phone-input'}))

    def clean_number(self):
        number = self.cleaned_data['number']        
        try:
            number=Recipient.objects.get(number__iexact=number)
            raise forms.ValidationError("That number is already registered to recieve CatFacts.")
        except Recipient.DoesNotExist:
            pass
        return number