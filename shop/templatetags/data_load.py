from django import template
from django.shortcuts import render, redirect
from django.db.models import Sum, Count, Q
from shop import models
from shop.views import get_client_ip
import uuid, socket 

register = template.Library()

@register.filter(name='company')
def company_details(request):
    company = models.CompanyInfo.objects.filter(status=True)
    return company

@register.filter(name='branch_list')
def branch_details(request):
    branch = models.Branches.objects.filter(status=True)
    return branch

@register.filter(name='product_menu')
def category_menu(request):
    product = models.Products.objects.filter(status = True).order_by('cat_name','cat_name__cat_name','sub_cat_name', 'brand_name')
    return product

@register.filter(name='count_cart')
def count_cart_list(request):
    cart = models.AddToCart.objects.filter(mac_address = hex(uuid.getnode())).count()
    return cart

@register.filter(name='cart_amount')
def total_cart_amount(request):
    amount = models.AddToCart.objects.filter(ip_address = socket.gethostbyname(socket.gethostname()), mac_address = hex(uuid.getnode())).aggregate(Sum('total_price'))['total_price__sum']
    return amount

@register.filter(name='count_wish')
def count_wish_list(request):
    wish = models.Wishlist.objects.filter(ip_address = socket.gethostbyname(socket.gethostname()), mac_address = hex(uuid.getnode())).count()
    return wish

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
