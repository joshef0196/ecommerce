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
import uuid, socket, random
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request):   
    if request.is_ajax():
        search_by = (request.GET.get('search')).strip()
        category  = request.GET.get('category')
        product_list = models.Products.objects.values("id","product_name","product_image1").filter(product_name__icontains = search_by, status = True).order_by("-id")[:10] 
        return JsonResponse(list(product_list), safe = False)

    elif request.method=="POST":   
        search_by = (request.POST['search']).strip()
        cat_id   = int(request.POST['cat_id'])
    
        if cat_id == 0 and len(str(search_by)) > 0:
            product_list = models.Products.objects.filter(product_name__icontains = search_by, status = True).order_by("-id")

        else:
            product_list = models.Products.objects.filter(cat_name__cat_name_id = cat_id, status = True).order_by("-id")
        
        context = {
            'product_list' : product_list,
            'search' : search_by,
            'cat_id' : cat_id,
        }
        return render(request,"shop/search_product.html",context)

    else:
        about_us             = models.AboutUs.objects.filter(status = True).first()
        products_cat         = models.Products.objects.filter(status = True).order_by('cat_name__cat_name','ordering')
        popular_pro          = models.Products.objects.filter(status = True).order_by('ordering')
        recent_pro           = models.Products.objects.filter(status = True).order_by('-id')
        check_addtocat       = models.AddToCart.objects.filter(status = True).order_by('-id')
        seo_content          = models.SeoContent.objects.filter(status = True).first()
        slider               = models.SliderInfo.objects.filter(status = True).order_by('-slider_order').reverse()
        context = {
            'about_us'     : about_us,
            'products_cat' : products_cat,
            'popular_pro'  : popular_pro,
            'recent_pro'  : recent_pro,
            'check_addtocat'  : check_addtocat,
            'seo_content'  : seo_content,
            'slider'  : slider,
        }
        return render(request,'shop/index.html', context)
  
def contact(request):
    context = {
        'seo_content' : models.SeoContent.objects.filter(status = True).first(),
    }
    if request.method=="POST":
        name      = request.POST['name']
        email     = request.POST['email']
        phone     = request.POST['phone']
        subject   = request.POST['subject']
        message   = request.POST['message']
        if models.ContactUs.objects.create(customer_name = name, email_address = email, message = message, mobile = phone, subject = subject, ip_address = socket.gethostbyname(socket.gethostname())):
            messages.success(request,'Message Submitted')
            return redirect("/contact-us/")
        else :
            messages.error(request,'Submitted Fail')  
            return redirect("/contact-us/")
    
    return render(request,'shop/contact.html', context)
 
def about_us(request):
    about_us = models.AboutUs.objects.filter(status = True).first()
    context = {
        'about_us' : about_us,
    }
    return render(request,'shop/about_us.html', context)
 
def registration(request):
    if request.method=="POST":
        user_name    = request.POST['user_name']
        email        = request.POST['email']
        password     = request.POST['password']
        mobile       = request.POST['mobile']
        address      = request.POST['address']

        new_md5_obj  = hashlib.md5(password.encode())
        new_enc_pass = new_md5_obj.hexdigest()
        chk_email = models.UserRegistration.objects.filter(user_email = email)
        
        if not chk_email:
            models.UserRegistration.objects.create(user_name = user_name, user_email = email, user_password = new_enc_pass, user_mobile = mobile, address = address)
            messages.success(request,'Thank you for registering.')
            return redirect("/account/login/")
        else :
            messages.error(request,'Registration Fail.Please input valid value.')  
            return redirect("/account/register/")
    else:
        context = {
            'seo_content' : models.SeoContent.objects.filter(status = True).first(),
        }
    return render(request,'shop/registration_form.html', context)
 
def login(request):
    if request.method=="POST":
        email     = request.POST['email']
        password  = request.POST['password']

        new_md5_obj = hashlib.md5(password.encode())
        enc_pass    = new_md5_obj.hexdigest()
        user        = models.UserRegistration.objects.filter(user_email = email, user_password = enc_pass, status = True)
        if user:
            request.session['user_email']   = user[0].user_email
            return redirect('/address-book/') 
        else:
            messages.error(request,"Email and Password incorrect.")  
            return redirect('/account/login/') 

    return render(request,'shop/login.html')
 
def forgot_password(request):
    if not request.session['user_email']:
        return redirect('/account/login/')
        
    if request.method == "POST":
        current_pass = request.POST['current_pass']
        new_pass     = request.POST['new_pass']

        new_md5_obj = hashlib.md5(current_pass.encode())
        new_enc_pass = new_md5_obj.hexdigest()
        chk_user     = models.UserRegistration.objects.filter(id = request.session['id'], password = new_enc_pass)
        if chk_user:
            new_md5_obj = hashlib.md5(new_pass.encode())
            new_enc_pass = new_md5_obj.hexdigest()
            models.UserRegistration.objects.filter(id = request.session['id']).update(password = new_enc_pass)
            messages.success(request,'Your password has been changed.')
            return redirect("/change-my-password/")
        else:
            messages.error(request,'Invalid current Password')
            return redirect("/change-my-password/")

    return render(request,'shop/account/forgot_password.html')

def logout(request):  
    request.session['user_email']  = False
    return redirect('/account/login/')

 
def my_address_book(request):
    if not request.session['user_email']:
        return redirect('/account/login/')

    address = models.UserRegistration.objects.filter(user_email = request.session["user_email"]).first()
    context = {
        'address' : address,
    }
    return render(request,'shop/address_book.html', context)

def edit_address_book(request, id):
    address = models.AddressBook.objects.filter(id = id)
    context = {
        'address':address,
    }
    if request.method == "POST":
        full_name   = request.POST['full_name']
        phone       = request.POST['phone_number']
        region      = request.POST['region']
        city        = request.POST['city']
        area        = request.POST['area']
        address     = request.POST['address']
        models.AddressBook.objects.filter(id = id).update(full_name = full_name, phone_number = phone, region = region, city = city,  area = area, address = address)
        return redirect('/address-book/')

    return render(request, "shop/edit_address_book.html",context)   

def my_account(request):
    if not request.session['user_email']:
        return redirect('/account/login/')

    address = models.UserRegistration.objects.filter(status = True)
    context = {
        'address' : address,
    }
    return render(request,'shop/my_account.html', context)
 
def order_history(request):
    if not request.session['user_email']:
        return redirect('/account/login/')

    history = models.AddToCart.objects.filter(ip_address= socket.gethostbyname(socket.gethostname()), mac_address = hex(uuid.getnode()))
    context = {
        'history' : history,
    }
    return render(request,'shop/order_history.html', context)
 
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
    offer = models.OfferProduct.objects.filter(status = True)
    context = {
        'offer' : offer,
        'seo_content' : models.SeoContent.objects.filter(status = True).first(),
    }
    return render(request,'shop/offers.html', context)

def single_offers(request, id):
    single_offer = models.OfferProduct.objects.filter(id = id).first()
    context = {
        'single_offer' : single_offer,
    }
    return render(request,'shop/single_offers.html', context)

def faq(request):
    privacy_policy = models.PrivacyPolicy.objects.filter(status = True).first()
    context = {
        'privacy_policy' : privacy_policy,
    }
    return render(request,'shop/faq.html', context)

def wishlist(request):
    context = {
        'wish_products': models.Wishlist.objects.filter(ip_address= socket.gethostbyname(socket.gethostname()), mac_address = hex(uuid.getnode())),
        'total_price': models.Wishlist.objects.filter(ip_address= socket.gethostbyname(socket.gethostname()), mac_address = hex(uuid.getnode())).aggregate(Sum('total_price'))['total_price__sum'],
    }
    return render(request,'shop/account/wishlist.html', context)

def cart_list(request):
    context = {
        'cart_products': models.AddToCart.objects.filter(ip_address = socket.gethostbyname(socket.gethostname()), mac_address = hex(uuid.getnode())),
        'total_price': models.AddToCart.objects.filter(ip_address = socket.gethostbyname(socket.gethostname()), mac_address = hex(uuid.getnode())).aggregate(Sum('total_price'))['total_price__sum'],
    }
    return render(request,'shop/account/cart.html', context)

def add_to_cart(request, id):
    product     = models.Products.objects.get(id = id)
    cart        = models.AddToCart.objects.filter(product_name_id = id, ip_address= socket.gethostbyname(socket.gethostname()), mac_address = hex(uuid.getnode()))
    if cart:
        messages.success(request,'Cart successfully updated')
        models.AddToCart.objects.filter(id = cart[0].id).update(quantity = F('quantity') + 1 , total_price = F('total_price') + cart[0].qt_price)
    else:    
        messages.success(request,'Product successfully added to cart')
        models.AddToCart.objects.create(product_name_id = id, mac_address = hex(uuid.getnode()), qt_price = product.price, total_price = product.price, ip_address = socket.gethostbyname(socket.gethostname()))

    return redirect("/")  

def add_to_wish(request, id):
    product     = models.Products.objects.get(id = id)
    models.Wishlist.objects.create(product_name_id = id, total_price = product.price, mac_address = hex(uuid.getnode()), ip_address = socket.gethostbyname(socket.gethostname()))
    return redirect("/")  

def delete_to_wish(request, id):
    models.Wishlist.objects.filter(id = id).delete()
    return redirect("/wishlist/")    

def delete_to_cart(request, id):
    models.AddToCart.objects.filter(id = id).delete()
    return redirect("/cart-list/")    

def checkout(request):
    cart_list = models.AddToCart.objects.filter(ip_address= socket.gethostbyname(socket.gethostname()), mac_address = hex(uuid.getnode()))

    if request.is_ajax():
        create_account = True if request.GET.get("create_account") else False
        full_name      = request.GET.get("cus_name")
        cus_email      = request.GET.get("cus_email")
        mobile         = request.GET.get("cus_phone")
        city           = request.GET.get("cus_city")
        zip_code       = request.GET.get("cus_postcode")
        address        = request.GET.get("cus_add1")

        last_order =  models.SalesHistory.objects.last()  
        if last_order:
            num        = ''.join(filter(lambda x: x.isdigit(), last_order.invoice_no))
            invoice_no = "CCTECH"+str(int(num)+1)    
        else: 
            invoice_no = "CCTECH"+str(int(100001)) 

        if create_account:
            new_md5_obj  = hashlib.md5(str(request.GET.get("password")).encode())
            new_enc_pass = new_md5_obj.hexdigest()
            models.UserRegistration.objects.create(
                user_name = full_name, user_email = cus_email, user_password = new_enc_pass, 
                user_mobile = mobile, city = city, address = address
            )
        sales_list = []    
        for i in cart_list:
            sales = models.SalesHistory.objects.create(
                    full_name = full_name, email = cus_email, mobile = mobile, city = city, zip_code = zip_code,
                    address = address, invoice_no = invoice_no, product_id = i.product_name_id, quantity = i.quantity, total_price = i.total_price
                )
            sales_list.append(sales)    
        if sales_list:
            cart_list.delete()
            data = {
                'status':'success',
                'invoice_no':invoice_no,
                'cus_email':cus_email,
            }
            return JsonResponse(data, safe = False)
        else:    
            data = {
                'status':'fail'
            }
            return JsonResponse(data, safe = False)

    context = {
        'cart_list': cart_list,
        'total_price':models.AddToCart.objects.filter(ip_address= socket.gethostbyname(socket.gethostname()), mac_address = hex(uuid.getnode())).aggregate(Sum('total_price'))['total_price__sum']
    }
    return render(request,'shop/account/checkout.html', context)

@csrf_exempt
def payment_cancel(request):
    print('request details', request)
    context = {
        'company_info': models.CompanyProfile.objects.all().last(),
    }
    return render(request, 'shop/account/payment_cancel.html',context)
    
@csrf_exempt
def payment_fail(request):
    print('request details', request)
    context = {
        'company_info': models.CompanyProfile.objects.all().last(),
    }
    return render(request, 'shop/account/payment_fail.html',context)

@csrf_exempt
def payment_successful(request):
    if request.method=="POST":
        full_name           = request.POST['opt_a']
        customer_email      = request.POST['opt_b']
        transaction_id      = str(request.POST['mer_txnid'])
        mobile              = transaction_id[:11]
        # gender              = request.GET['gender']
        # nid_or_passpord     = request.GET['cus_state']
        invoice_no          = transaction_id # aamarpay unique transaction id
        aamar_pay_txd_id    = request.POST['pg_txnid'] # aamarpay unique transaction id
        address             = request.POST['opt_d']
        # zip_code            = request.POST['mer_txnid'] #Merchant transaction id
        # city                = str(request.POST['pay_time'])
        split_trxd_id       = transaction_id[:12]
        ticket_quantity     = int(split_trxd_id[-1:])
        ticket_price        = float(request.POST['amount'])
        store_amount        = float(request.POST['store_amount'])
        last_ticket         = models.SalesHistory.objects.last()

        models.SalesHistory.objects.filter(invoice_no = invoice_no).update(status = True)
        order = models.SalesHistory.objects.filter(invoice_no = invoice_no, status = True).first()

        # html = """
        
        # Dear """+ order.full_name + """, 
        
        # """+ order.product.product_name + """ - Congratulations!! Your """+ str(order.product.cat_name) + """ ticket(s) purchase for ‘Signature of Rhythm’ has been successful by BDT """+ str(order.total_price) + """ ("""+ str(num2words(order.total_price)).title() + """) per ticket. 


        # See you on Friday, 22nd March, 2019.

        # """
        
        # # Creating message.
        # msg = MIMEMultipart('alternative')
        # msg['Subject'] = "Congratulations!Your ticket successfully bought"
        # msg['From']    = settings.EMAIL_HOST_USER
        # msg['To']      = order.email
        
        # # The MIME types for text/html
        # HTML_Contents = MIMEText(html, 'html')
        
        # # Attachment and HTML to body message.

        # msg.attach(HTML_Contents)
        
        # #set up the SMTP server
        # s = smtplib.SMTP(host='us2.smtp.mailhostbox.com', port=25)
        # s.starttls()
        # s.login(msg['From'], settings.EMAIL_HOST_PASSWORD)
        
        # s.sendmail(msg['From'], msg['To'], msg.as_string())
        # s.quit()
        
        messages.success(request,'Your order successfully placed')  
        
        context = {
            'order': order,
        } 
        return render(request, 'shop/account/order_complete.html', context)   
    return render(request, 'shop/account/order_complete.html') 

def order_complete(request):

    return render(request,'shop/account/order_complete.html')

def single_product(request, pro_name):
    pro            = pro_name.replace('-', ' ')
    single_pro     = models.Products.objects.filter(product_name = pro).first()
    if single_pro:
        related_post   = models.Products.objects.filter(brand_name_id = single_pro.brand_name_id, status=True).exclude(product_name = pro).order_by('-id')[:6]
    else:
        related_post = None
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
    pro_brand             = models.Brands.objects.filter(status = True).order_by('brand_name')

    context={
        'sub_sub_products':sub_sub_products,
        'pro_brand':pro_brand,
        'sub_sub_seo':sub_sub_products[0],
    }
    return render(request,'shop/sub_sub_products.html', context)

def insert_newsletter(request):
    if request.is_ajax():
        data = 'Something went wrong!'
        print('email ',request.GET['email'])
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', request.GET['email'])
        print('match', match)
        if match == None:
            data = 'Please input valid email address'
        else:
            if models.SubscriberNewslatter.objects.filter(subscriber_email=request.GET['email']).exists():
                data = 'Your have already subscribed'
            else:
                models.SubscriberNewslatter.objects.create(subscriber_email=request.GET['email'])
                data = 'Subscription Successful'
        return JsonResponse(data,safe=False)

