from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod
import math
from account import models as amod
from django import forms
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

@view_function
def process_request(request, product:cmod.Product):

    if request.method == 'POST':    
        form = QuantityForm(request.POST)
        form.Product = product
        form.user = request.user

        if request.user.is_authenticated:
    
        # Check if the form is valid:
            if form.is_valid():
                form.commit()
                return HttpResponseRedirect('/catalog/cart')
        else:
            return HttpResponseRedirect('/account/login')
    else:
        form = QuantityForm()

    categories = cmod.Category.objects.all()
    return request.dmp.render('product.html', {
        'product': product,
        'categories': categories,
        'form': form,
    })

@view_function
def tile(request, product:cmod.Product):
    return request.dmp.render('product.tile.html', {
        'product': product,
    })


class QuantityForm(forms.Form):
    quantity = forms.IntegerField(label = "Quantity")

    #create a clean method
    def clean(self):
        if self.user.is_authenticated:
            if self.cleaned_data.get('quantity') > self.Product.quantity:
                raise forms.ValidationError("Low inventory!")
        return self.cleaned_data
    
    def commit(self):
        cart = self.user.get_shopping_cart()
        saleitem = cmod.SaleItem.objects.filter(sale = cart, product = self.Product, status = 'A').first()

        if saleitem is None:
            saleitem = cmod.SaleItem()
            saleitem.sale = cart
            saleitem.product = self.Product
            saleitem.price = self.Product.price
            saleitem.quantity = self.cleaned_data.get('quantity')
        else:
            saleitem.quantity += self.cleaned_data.get('quantity')

        saleitem.save()
        cart.recalculate()
        cart.save()