from django.db import models

class Products(models.Model):

    product_name = models.CharField(max_length=225)
    price = models.IntegerField()
    image = models.ImageField(upload_to='product/images')
    description = models.CharField(max_length = 225,blank=True)
    
