from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    birthdate = models.DateTimeField(null=True)
    favcolor = models.TextField(null=True)

    def get_shopping_cart(self):
        from catalog import models as cmod
        return 0
    # retrieve (or create) a Sale with purchased=None for this user
    # return the Sale object