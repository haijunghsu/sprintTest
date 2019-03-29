from django.db import models
from django.contrib.auth.models import AbstractUser
from catalog import models as cmod

# Create your models here.
class User(AbstractUser):
    birthdate = models.DateTimeField(null=True)
    favcolor = models.TextField(null=True)

    def get_shopping_cart(self):
        from catalog import models as cmod
        cart = cmod.Sale.objects.filter(user = self, purchased = None).first()

        if cart is None:
            cart = cmod.Sale()
            cart.user = self
            cart.save()

        return cart