from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm

from service.models import Service


class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)
    hour = models.DateTimeField()

    def __str__(self):
        return self.service



    @property
    def price(self):
        return (self.service.price)

class ShopCartForm(ModelForm) :
    class Meta:
        model = ShopCart
        fields = ['hour']
