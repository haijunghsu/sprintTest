from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod
import math

ITEMS_PER_PAGE = 2

@view_function
def process_request(request, category:cmod.Category=None, page:int=1):
    categories = cmod.Category.objects.all()
    products = cmod.Product.objects.all()
    if category is not None:
        products = products.filter(category = category)
    products = products[(page - 1) * ITEMS_PER_PAGE: page * ITEMS_PER_PAGE]
    context = {
        # sent to index.html:
        'categories': categories,
        'category': category,
        'products': products,
        'page': page,
        'numpages': math.ceil(products.count()/ITEMS_PER_PAGE),
    }
    return request.dmp.render('index.html', context)


















# @view_function
# def process_request(request, category:cmod.Category=None, page:int=1):
#     products = cmod.Product.objects.all()
#     if category is not None:
#         products = products.filter(category=category)

#     return request.dmp.render('index.html', {
#         'category': category,
#         'products': products,
#         'page': page,
#         'numpages': math.ceil(products.count()/ITEMS_PER_PAGE),
#     })

    # IMAGES = [
    # "canvas.jpg",
    # "car.jpg",
    # "carrots.jpg",
    # "doll.jpg",
    # "door.jpg",
    # "drawer.jpg",
    # "drill_press.jpg",
    # "earser.jpg",
    # "eye_liner.jpg",
    # "face_wash.jpg",
    # "fake_flowers.jpg",
    # "flowers.jpg",
    # "food.jpg",
    # "pencil.jpg",
    # "perfume.jpg",
    # "phone.jpg",
    # "photo_album.jpg",
    # "piano.jpg",
    # "picture_frame.jpg",
    # "playing_card.jpg",
    # "pool_stick.jpg",
    # "television.jpg",
    # "puddle.jpg",
    # "purse.jpg",]
#the code to create 4 categories
    # for i in range(4):
    #     category = cmod.Category()
    #     category.name = f'testCat{i}'
    #     category.save()
#the code to create 6 products in each category, 3 images in each prouduct
    # pi = 0
    # for i in range(6):
    #     product = cmod.Product()
    #     product.category = cmod.Category.objects.get(name = 'testCat0')
    #     product.name = f'0product{i}'
    #     product.description = f'some description for 0 product{i}'
    #     product.price = 10 + 10 * i
    #     product.quantity  = 100 - 10 * i
    #     product.reorder_trigger = 2
    #     product.reorder_quantity = 5
    #     product.save()
    #     for j in range(3):
    #         productimage = cmod.ProductImage()
    #         productimage.product = cmod.Product.objects.get(name = f'0product{i}')
    #         productimage.filename = IMAGES[pi]
    #         productimage.save()
    #         pi += 1
