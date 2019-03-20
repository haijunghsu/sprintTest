from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod
import math

ITEMS_PER_PAGE = 8

@view_function
def process_request(request, category:cmod.Category=None, page:int=1):



    IMAGES = ["apple.jpg",
    "bag.jpg",
    "balloon.jpg",
    "bananas.jpg",
    "bed.jpg",
    "beef.jpg",
    "bookmark.jpg",
    "boom_box.jpg",
    "bottle_cap.jpg",
    "bow.jpg",
    "bowl.jpg",
    "bracelet.jpg",
    "bread.jpg",
    "buckel.jpg",
    "button.jpg",
    "camera.jpg",
    "candle.jpg",
    "candy_wrapper.jpg",
    "canvas.jpg",
    "car.jpg",
    "carrots.jpg",
    "cat.jpg",
    "cell_phone.jpg",
    "chair.jpg",
    "chapter_book.jpg",
    "charger.jpg",
    "checkbook.jpg",
    "chocolate.jpg",
    "cinder_block.jpg",
    "clock.jpg",
    "clothes.jpg",
    "coasters.jpg",
    "computer.jpg",
    "conditioner.jpg",
    "controller.jpg",
    "cookie_jar.jpg",
    "cork.jpg",
    "couch.jpg",
    "credit_card.jpg",
    "cup.jpg",
    "desk.jpg",
    "doll.jpg",
    "door.jpg",
    "drawer.jpg",
    "drill_press.jpg",
    "earser.jpg",
    "eye_liner.jpg",
    "face_wash.jpg",
    "fake_flowers.jpg",
    "floor.jpg",
    "flowers.jpg",
    "food.jpg",
    "fork.jpg",
    "fridge.jpg",
    "glass.jpg",
    "glasses.jpg",
    "glow_stick.jpg",
    "greeting_card.jpg",
    "grid_paper.jpg",
    "hair_tie.jpg",
    "headphones.jpg",
    "ice_cube_tray.jpg",
    "ipod.jpg",
    "key_chain.jpg",
    "keyboard.jpg",
    "keys.jpg",
    "knife.jpg",
    "lace.jpg",
    "lamp.jpg",
    "lamp_shade.jpg",
    "leg_warmers.jpg",
    "lip_gloss.jpg",
    "lotion.jpg",
    "magnet.jpg",
    "milk.jpg",
    "mirror.jpg",
    "monitor.jpg",
    "mp3_player.jpg",
    "nail_clippers.jpg",
    "nail_file.jpg",
    "needle.jpg",
    "newspaper.jpg",
    "notfound.jpg",
    "outlet.jpg",
    "packing_peanuts.jpg",
    "paper.jpg",
    "pen.jpg",
    "pencil.jpg",
    "perfume.jpg",
    "phone.jpg",
    "photo_album.jpg",
    "piano.jpg",
    "picture_frame.jpg",
    "playing_card.jpg",
    "pool_stick.jpg",
    "puddle.jpg",
    "purse.jpg",
    "radio.jpg",
    "rubber_band.jpg",
    "rubber_duck.jpg",
    "rug.jpg",
    "sand_paper.jpg",
    "sharpie.jpg",
    "shawl.jpg",
    "shoe_lace.jpg",
    "shoes.jpg",
    "sidewalk.jpg",
    "sketch_pad.jpg",
    "slipper.jpg",
    "soap.jpg",
    "socks.jpg",
    "soda_can.jpg",
    "sofa.jpg",
    "speakers.jpg",
    "spoon.jpg",
    "spring.jpg",
    "sticky_note.jpg",
    "stockings.jpg",
    "stop_sign.jpg",
    "street_lights.jpg",
    "sun_glasses.jpg",
    "television.jpg",
    "thermometer.jpg",
    "thermostat.jpg",
    "thread.jpg",
    "tire_swing.jpg",
    "toilet.jpg",
    "tomato.jpg",
    "tooth_picks.jpg",
    "toothbrush.jpg",
    "toothpaste.jpg",
    "towel.jpg",
    "tree.jpg",
    "truck.jpg",
    "tv.jpg",
    "twezzers.jpg",
    "twister.jpg",
    "vase.jpg",
    "video_games.jpg",
    "wagon.jpg",
    "wallet.jpg",
    "washing_machine.jpg",
    "water_bottle.jpg",
    "white_out.jpg",
    "window.jpg",
    "zipper.jpg",]
#the code to create 6 products in each category, 3 images in each prouduct
    # pi = 0
    # for i in range(30):
    #     product = cmod.Product()
    #     product.category = cmod.Category.objects.get(name = 'testCat3')
    #     product.name = f'3product{i}'
    #     product.description = f'some description for 3product{i}'
    #     product.price = 10 + 10 * i
    #     product.quantity  = 200 - 10 * i
    #     product.reorder_trigger = 2
    #     product.reorder_quantity = 5
    #     product.save()
    #     for j in range(3):
    #         productimage = cmod.ProductImage()
    #         productimage.product = cmod.Product.objects.get(name = f'3product{i}')
    #         productimage.filename = IMAGES[4*i - pi]
    #         productimage.save()
    #         pi += 1



    categories = cmod.Category.objects.all()
    products = cmod.Product.objects.all()
    numpages = math.ceil(products.count()/ITEMS_PER_PAGE)
    if category is not None:
        products = products.filter(category = category)
        numpages = math.ceil(products.count()/ITEMS_PER_PAGE)
    products = products[(page - 1) * ITEMS_PER_PAGE: page * ITEMS_PER_PAGE]
    context = {
        # sent to index.html:
        'categories': categories,
        'category': category,
        'products': products,
        'page': page,
        'numpages': numpages,
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

