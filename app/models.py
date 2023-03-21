from django.utils import timezone

from django.db import models



class Product(models.Model):
    title = models.CharField(max_length=255)
    size = models.TextField(default='DEFAULT_VALUE')
    manufactur = models.CharField(max_length=255, default='DEFAULT_VALUE')
    price = models.CharField(max_length=255)
    time_create = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)



    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return str(self.id)

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return str(self.name)


class Manufacturer(models.Model):
    firm = models.CharField(max_length=255, default="DEFAULT_VALUE")
    country = models.CharField(max_length=100)