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
        # Check if the form is valid:
        if form.is_valid():
            # login(request, form.user)
            #get_user_shopping cart
            #make new sale item
            return HttpResponseRedirect('/catalog/cart/')
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
    purchase_quantity = forms.CharField(help_text = "Enter your quantity")

    #create a clean method
    # def clean(self):

    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')

    #     self.user = authenticate(username = username, password = password)

    #     if self.user is not None:
    #         return self.cleaned_data
    #     else:
    #         raise forms.ValidationError('your username or password is not correct')