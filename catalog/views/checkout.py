from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from account import models as amod
from django import forms
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from catalog.views.forms import ProductForm
from catalog import models as cmod


class CheckoutForm(forms.Form):
    address = forms.CharField(label='Shipping Address')
    city = forms.CharField(label='Shipping City')
    state = forms.CharField(label = 'Shipping State')
    zipcode = forms.CharField(label='Shipping')
    stripeToken = forms.CharField(widget=forms.HiddenInput())

    def clean(self):
        try: self.sale.finalize(self.cleaned_data['stripeToken'])
        except Exception as e:
            raise forms.ValidationError('Error processing payment: {}'.format(e))

@view_function
def process_request(request):
    cart = request.user.get_shopping_cart()
    cart.save()

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        form.sale = request.user.get_shopping_cart()

        if form.is_valid():
            
            return HttpResponseRedirect('/catalog/receipt/{}'.format(form.sale.id)) 
    else:
        form = CheckoutForm()    

    categories = cmod.Category.objects.all()
    context = {'form':form,
    'categories':categories,
    'cart':cart}

    return request.dmp.render('checkout.html', context)        