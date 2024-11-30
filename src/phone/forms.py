from django import forms
from .models import Brand, Mobile


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'nationality']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'name': 'Enter the brand name',
            'nationality': 'Enter the nationality of the brand',
        }

    def clean_nationality(self):
        nationality = self.cleaned_data['nationality']
        if not nationality.isalpha():
            raise forms.ValidationError("Nationality must contain only alphabetic characters")
        return nationality


class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = ['brand', 'model', 'price', 'color', 'screen_size', 'availability_status', 'assembling_country']
        widgets = {
            'brand': forms.Select(attrs={'class': 'form-select'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'screen_size': forms.NumberInput(attrs={'class': 'form-control'}),
            'availability_status': forms.Select(attrs={'class': 'form-select'}),
            'assembling_country': forms.TextInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'brand': 'Select the brand of the mobile phone',
            'model': 'Enter the model name or number',
            'price': 'Enter the price of the mobile',
            'color': 'Specify the color of the mobile',
            'screen_size': 'Enter the screen size',
            'availability_status': 'Select whether the mobile is available or unavailable',
            'assembling_country': 'Specify the country where the mobile is assembled',
        }

    def clean_assembling_country(self):
        assembling_country = self.cleaned_data['assembling_country']
        if not assembling_country.isalpha():
            raise forms.ValidationError("Assembling country must contain only alphabetic characters")
        return assembling_country

    def clean_color(self):
        color = self.cleaned_data['color']
        if not color.isalpha():
            raise forms.ValidationError("Color must contain only alphabetic characters")
        return color


# Form of first task
class NationalitySearchForm(forms.Form):
    nationality = forms.CharField(max_length=255, label="Enter Nationality")


# Form of second task
class SearchBrandForm(forms.Form):
    brand_name = forms.CharField(max_length=255, label="Enter Brand Name")


# Form of fourth task
class NotesForm(forms.Form):
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 60}), label="Your Notes")
