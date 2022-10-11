from email.policy import default
from django.db import models

from store.models import Products

class Cart(models.Model):

    product = models.ForeignKey(Products,on_delete = models.CASCADE)
    quantity = models.IntegerField(default=0)
   


    def get_price(self):

        return self.product.price * self.quantity

