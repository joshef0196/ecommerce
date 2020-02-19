from django.shortcuts import render,redirect,HttpResponse
from . import models
from django.contrib import messages
from django.db.models import Sum
from django.db.models import F,Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import datetime, hashlib, socket, string, os, re
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):

    return render(request,'shop/index.html')
 
def contact(request):

    return render(request,'shop/contact.html')
 
def about_us(request):
    about_us = models.AboutUs.objects.filter(status = True).first()
    context = {
        'about_us' : about_us,
    }
    return render(request,'shop/about_us.html', context)
 
def emi(request):
    emi = models.Emi.objects.filter(status = True).first()
    context = {
        'emi' : emi,
    }
    return render(request,'shop/emi.html', context)
 
def warranty(request):
    warranty = models.Warranty.objects.filter(status = True).first()
    context = {
        'warranty' : warranty,
    }
    return render(request,'shop/warranty.html', context)

def payment_method(request):
    payment_method = models.PaymentMethod.objects.filter(status = True).first()
    context = {
        'payment_method' : payment_method,
    }
    return render(request,'shop/payment_method.html', context)
 
def terms_conditions(request):
    terms_conditions = models.TermsConditions.objects.filter(status = True).first()
    context = {
        'terms_conditions' : terms_conditions,
    }
    return render(request,'shop/terms_conditions.html', context)

def return_refund_policy(request):
    return_refund_policy = models.ReturnRefundPolicy.objects.filter(status = True).first()
    context = {
        'return_refund_policy' : return_refund_policy,
    }
    return render(request,'shop/return_refund_policy.html', context)

def privacy_policy(request):
    privacy_policy = models.PrivacyPolicy.objects.filter(status = True).first()
    context = {
        'privacy_policy' : privacy_policy,
    }
    return render(request,'shop/privacy_policy.html', context)

def offers(request):
    privacy_policy = models.PrivacyPolicy.objects.filter(status = True).first()
    context = {
        'privacy_policy' : privacy_policy,
    }
    return render(request,'shop/offers.html', context)

def faq(request):
    privacy_policy = models.PrivacyPolicy.objects.filter(status = True).first()
    context = {
        'privacy_policy' : privacy_policy,
    }
    return render(request,'shop/faq.html', context)

def wishlist(request):
    privacy_policy = models.PrivacyPolicy.objects.filter(status = True).first()
    context = {
        'privacy_policy' : privacy_policy,
    }
    return render(request,'shop/account/wishlist.html', context)

def cart_list(request):
    
    return render(request,'shop/account/cart.html')

def checkout(request):

    return render(request,'shop/account/checkout.html')

def order_complete(request):

    return render(request,'shop/account/order_complete.html')

def single_product(request, pro_name):
    pro            = pro_name.replace('-', ' ')
    single_pro     = models.Products.objects.filter(product_name = pro).first()
    related_post   = models.Products.objects.filter(brand_name_id = single_pro.brand_name_id, status=True).exclude(product_name = pro).order_by('-id')[:6]
    context={
        'single_pro':single_pro,
        'related_post':related_post,
    }
    return render(request,'shop/single_product.html', context)
 
def products_cat(request, cat_name):
    category          = cat_name.replace('-', ' ')
    product_cat       = models.Products.objects.filter(cat_name__cat_name__cat_name = category, status = True).order_by('cat_name__cat_name__cat_name')
    pro_brand         = models.Brands.objects.filter(status = True).order_by('brand_name')

    context={
        'product_cat':product_cat,
        'pro_brand':pro_brand,
    }
    return render(request,'shop/products_cat.html', context)
 
def sub_products(request, cat_name, sub_name):
    category              = cat_name.replace('-', ' ')
    sub_category          = sub_name.replace('-', ' ')
    product_sub_cat       = models.Products.objects.filter(cat_name__cat_name__cat_name = category, cat_name__sub_category = sub_category, status = True).order_by('cat_name__sub_category')
    pro_brand             = models.Brands.objects.filter(status = True).order_by('brand_name')

    context={
        'product_sub_cat':product_sub_cat,
        'pro_brand':pro_brand,
    }
    return render(request,'shop/sub_products.html', context)
 
def sub_sub_products(request, cat_name, sub_name, sub_sub_name):
    category              = cat_name.replace('-', ' ')
    sub_category          = sub_name.replace('-', ' ')
    sub_sub_category      = sub_sub_name.replace('-', ' ')
    sub_sub_products      = models.Products.objects.filter(cat_name__cat_name__cat_name = category, cat_name__sub_category = sub_category, sub_cat_name__sub_category = sub_sub_category, status = True).order_by('id')

    context={
        'sub_sub_products':sub_sub_products,
    }
    return render(request,'shop/sub_sub_products.html', context)

