# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers  import reverse
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length= 255)
    slug = models.SlugField(unique = True )
    description = models.TextField()
    is_active = models.BooleanField()
    meta_keywords = models.CharField(max_length = 100)
    meta_description = models.CharField(max_length = 100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    class Meta:
        db_table = 'Categories'
        ordering =['created_at']
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return reverse("category", kwargs={"slug":self.slug})

class Product(models.Model):
    name = models.CharField(max_length = 255)
    slug  = models.SlugField(unique = True)
    sku = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits=9,decimal_places=2 , default=0.00)
    old_price = models.DecimalField(max_digits = 9 , decimal_places=2)
    image = models.CharField(max_length=100)
    is_active = models.BooleanField()
    is_bestseller = models.BooleanField()
    is_featured = models.BooleanField()
    quantity = models.IntegerField()
    description = models.TextField()
    meta_keywords = models.CharField(max_length = 100)
    meta_description = models.CharField(max_length = 100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    categories = models.ManyToManyField(Category)

    @models.permalink
    def get_absolute_url(self):
        return reverse("products", kwargs={"slug":self.slug})
    
    def __unicode__(self):
        return self.name
    
    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None



    

