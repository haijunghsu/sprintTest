from django import forms
from catalog import models as pmod
from account import models as amod

class ProductForm(forms.Form):
    quantity_to_purchase = forms.IntegerField(label = 'Quantity')

    def clean(self):
        product_quantity = self.cleaned_data.get('quantity_to_purchase')
        if amod.User.is_authenticated:
            raise forms.ValidationError('You are not logged in!')

        if product_quantity > self.pmod.Product.quantity:
            raise forms.ValidationError('Inventory too low!')
        return self.cleaned_data 