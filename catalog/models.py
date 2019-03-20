from django.db import models

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