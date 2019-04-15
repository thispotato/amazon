# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render , get_object_or_404
from .models import Category , Product
from .forms import ProductForm

def index(request):
    page_title = 'This is the store'
    return render (request , 'catalog/index.html', locals())

def product(request , product_slug):
    p = get_object_or_404(Product , slug=product_slug)
    categories = p.categories.filter(is_active=True)
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description

    return render(request , 'catalog/product.html' , locals())

def category(request , category_slug):
    cat = get_object_or_404(Category , slug=category_slug)
    prod = cat.product_set.all()
    page_title = cat.name
    meta_keywords = cat.meta_keywords
    meta_description = cat.meta_description

    return render(request , 'catalog/category.html' , locals())

