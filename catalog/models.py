from django.db import models
from decimal import Decimal

# Create your models here.
class Category(models.Model):
    last_modified = models.DateTimeField(auto_now=True)
    name = models.TextField()

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #check on this
    last_modified = models.DateTimeField(auto_now=True)
    status = models.TextField(db_index=True, choices=(('A','Active'),('I','Inactive')), default= "Active") #check on this
    name = models.TextField()
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=15,decimal_places=2)
    quantity = models.IntegerField()
    reorder_trigger = models.IntegerField()
    reorder_quantity = models.IntegerField()

    def image_url(self): #check
        return self.image_urls()[0]

    def image_urls(self): #check
        pimages = ProductImage.objects.filter(product=self)
        urls = []
        for p in pimages:
            urls.append(p.image_url())
        
        if len(urls) == 0: 
            urls.append('catalog/media/products/notfound.jpg')
        return urls
        # else:
        #     return urls

class ProductImage(models.Model):
    filename = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    def image_url(self): #check
        return('catalog/media/products/' + self.filename)


TAX_RATE = Decimal("0.05")

class Sale(models.Model):
    user = models.ForeignKey("account.User", on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    purchased = models.DateTimeField(null=True, default=None)
    subtotal = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
    tax = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
    total = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
    charge_id = models.TextField(null=True, default=None)   # successful charge id from stripe

    def recalculate(self):
        #'''Recalculates the subtotal, tax, and total fields. Does not save the object.'''
        # complete this method!
        return 0

    def finalize(self, stripeToken):
        #'''Finalizes the sale'''
        # complete this method!
        # Ensure this sale isn't already finalized (purchased should be None)
        if self.purchased is not None:
            raise ValueError('this sales has already been finalized')
        # Check product quantities one more time
        # Call recalculate one more time
        # Create a charge using the `stripeToken` (https://stripe.com/docs/charges)
            # be sure to pip install stripe and import stripe into this file
        # Set purchased=now and charge_id=the id from Stripe
        # Save
        return 0


class SaleItem(models.Model):
    STATUS_CHOICES = [
        ( 'A', 'Active' ),
        ( 'D', 'Deleted' ),
    ]
    status = models.CharField(max_length=1, default=STATUS_CHOICES[0][0], choices=STATUS_CHOICES)
    sale = models.ForeignKey("Sale", on_delete=models.PROTECT, related_name="items")
    product = models.ForeignKey("Product", on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
    class Meta:
        ordering = [ 'product__name' ]