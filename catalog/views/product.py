from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod
import math

@view_function
def process_request(request, product:cmod.Product):
    categories = cmod.Category.objects.all()
    return request.dmp.render('product.html', {
        'product': product,
        'categories': categories,
    })

@view_function
def tile(request, product:cmod.Product):
    return request.dmp.render('product.tile.html', {
        'product': product,
    })