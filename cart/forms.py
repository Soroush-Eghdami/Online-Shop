from django import forms

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1, max_value=20,
        widget=forms.NumberInput(attrs={'class': 'quantity-input'})
    )
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label='Quantity')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)