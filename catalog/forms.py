from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product


class ProductForm(ModelForm):
    FORBIDDEN_WORDS = [
        'казино', 'криптовалюта', 'крипта', 'биржа',
        'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
    ]

    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Название продукта',
            'description': 'Описание продукта',
            'price': 'Цена',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите имя'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание'
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену товара'
        })

    def clean_name(self):
        """Валидация названия продукта"""
        name = self.cleaned_data.get('name', '').lower()

        for forbidden_word in self.FORBIDDEN_WORDS:
            if forbidden_word in name:
                raise ValidationError(
                    f'Название не может содержать запрещенное слово: "{forbidden_word}"'
                )

        return self.cleaned_data['name']

    def clean_description(self):
        """Валидация описания продукта"""
        description = self.cleaned_data.get('description', '').lower()

        for forbidden_word in self.FORBIDDEN_WORDS:
            if forbidden_word in description:
                raise ValidationError(
                    f'Описание не может содержать запрещенное слово: "{forbidden_word}"'
                )

        return self.cleaned_data['description']

    def clean_price(self):
        """Валидация цены продукта"""
        price = self.cleaned_data.get('price')

        if price is not None and price < 0:
            raise ValidationError('Цена не может быть отрицательной')

        return price
