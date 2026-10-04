from django import forms
from .models import Food


class Form(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'calories']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border border-gray-300 px-4 py-3 focus:outline-none focus:ring-2 focus:ring-orange-500',
                'placeholder': 'e.g. Chicken'
            }),

            'calories': forms.NumberInput(attrs={
                'class': 'w-full rounded-lg border border-gray-300 px-4 py-3 focus:outline-none focus:ring-2 focus:ring-orange-500',
                'placeholder': 'e.g. 350',
                'min': '1'
            }),
        }