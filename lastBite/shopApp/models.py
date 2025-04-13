from django.db import models

class Goods(models.Model):
    goodName = models.CharField(max_length=100, default="Название товара")
    goodPic = models.ImageField(upload_to='goods/', blank=True, null=True)
    price = models.IntegerField(default=100)

