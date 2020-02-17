from django import template
from django.shortcuts import render, redirect
from django.db.models import Sum, Count, Q
from shop import models
register = template.Library()

@register.filter(name='company')
def company_details(request):
    company = models.CompanyInfo.objects.filter(status=True)
    return company

@register.filter(name='product_menu')
def category_menu(request):
    product = models.Products.objects.filter(status = True).order_by('cat_name','cat_name__cat_name','sub_cat_name', 'brand_name')
    return product

@register.filter(name='str2url')
def string_to_url_convert(data):
    #use in view: category = cat.replace('-', ' ')
    # use in html: text|str2url
    data = str(data)    
    return data.replace(' ', '-') 

@register.filter(name='replace')
def replace_load(obj):
    rep = obj.replace("%20"," ")
    return rep
