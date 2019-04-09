from catalog import models as cmod
from django_mako_plus import view_function, jscontext
from django import forms
from django.http import HttpResponseRedirect

@view_function
def process_request(request):
   cart = request.user.get_shopping_cart()
   saleitems = cmod.SaleItem.objects.filter(sale = cart, status = 'A')
   sale = cmod.Sale()
   categories = cmod.Category.objects.all()
   context = {
       'categories': categories,
       'cart' : cart,
       'saleitems' : saleitems,
       'sale':sale,
   }

   return request.dmp.render('receipt.html', context)