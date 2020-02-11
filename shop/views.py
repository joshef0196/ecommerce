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
    return render(request,'shop/privacy_policy.html', context)

def single_product(request):

    return render(request,'shop/single_product.html')
 
