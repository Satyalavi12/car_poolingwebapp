from django import forms
from .models import Userdetails,URL
from django.core.exceptions import ValidationError

class UserdetailsForm(forms.ModelForm):
    distance = forms.DecimalField(label='Distance (in km)', min_value=0.0, decimal_places=2)
    distance_per_km = forms.DecimalField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Userdetails
        fields = ['Name', 'start', 'destination', 'via', 'phone_number', 'email', 'car_name', 'start_date_time', 'distance', 'distance_per_km']
        widgets = {
            'start_date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if len(phone_number) != 10:
            raise ValidationError("Phone number should have exactly 10 digits.")
        return phone_number


class URLForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ['url']
