import os
from django.db import models
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField

class CompanyInfo(models.Model):
    com_name     = models.CharField(max_length=100)
    staring_year = models.IntegerField(default=2020)
    email1       = models.CharField(max_length=100, blank=True)
    email2       = models.CharField(max_length=100, blank=True)
    website      = models.CharField(max_length=200, blank=True)
    phone        = models.CharField(max_length=15,  blank=True)
    mobile1      = models.CharField(max_length=15,  blank=True)
    mobile2      = models.CharField(max_length=15,  blank=True)
    address      = models.TextField(max_length=200, blank=True)
    facebook     = models.CharField(max_length=200, blank=True)
    twitter      = models.CharField(max_length=200, blank=True)
    linkedin     = models.CharField(max_length=200, blank=True)
    skype        = models.CharField(max_length=200, blank=True)
    youtube      = models.CharField(max_length=200, blank=True)
    com_details  = RichTextField(blank=True)
    status       = models.BooleanField(default=True)

    def __str__(self):
        return self.com_name

    class Meta:
        verbose_name = 'Company Info'
        verbose_name_plural = 'Company Information'

class SubscriberNewslatter(models.Model):
    subscriber_email = models.EmailField()
    subscirbe_date   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subscriber_email

    class Meta:
        verbose_name = 'News Letter'
        verbose_name_plural = 'Subscriber News Letters'

class SliderInfo(models.Model):
    slider_name   = models.CharField(max_length=100, blank=True)
    title1        = models.CharField(max_length=200, blank=True)
    title2        = models.CharField(max_length=200, blank=True)
    slider_images = models.ImageField(upload_to='images/slider')
    upload_date   = models.DateTimeField(auto_now_add=True)
    slider_order  = models.IntegerField()
    status        = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Slider Images'

    def url(self):
        return os.path.join('/static/shop/media/images/slider/', os.path.basename(str(self.slider_images)))

    def photo(self):
        return mark_safe('<img src = "{}" width="80"/>'.format(self.url()))

    def __str__(self):
        return self.slider_name

class Catagory(models.Model):
    cat_name        = models.CharField(max_length=50)   
    status          = models.BooleanField(default=True)
    def __str__(self):
        return self.cat_name

    class Meta:
        verbose_name = 'Catagory'
        verbose_name_plural = 'Catagories'        

class Brands(models.Model):
    brand_name      = models.CharField(max_length=50)   
    status          = models.BooleanField(default=True)
    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'        

class SubCatagory(models.Model):
    cat_name        = models.ForeignKey(Catagory, on_delete = models.CASCADE)
    sub_category    = models.CharField(max_length=50)
    details         = models.CharField(max_length=200, blank=True)
    meta_description= models.TextField(blank=True)
    meta_keywords   = models.TextField(blank=True)
    meta_title      = models.TextField(blank=True)    
    status          = models.BooleanField(default=1)
    def __str__(self):
        return self.sub_category

    class Meta:
        verbose_name = 'Catagory'
        verbose_name_plural = 'Sub Catagories'        

class SubSubCatagory(models.Model):
    cat_name        = models.ForeignKey(SubCatagory, on_delete = models.CASCADE)
    sub_category    = models.CharField(max_length=50)
    details         = models.CharField(max_length=100, blank=True)
    meta_description= models.TextField(blank=True)
    meta_keywords   = models.TextField(blank=True)
    meta_title      = models.TextField(blank=True)    
    status          = models.BooleanField(default=1)
    def __str__(self):
        return self.sub_category

    class Meta:
        verbose_name = 'Catagory'
        verbose_name_plural = 'Sub Sub Catagories'        

class Products(models.Model):
    cat_name       = models.ForeignKey(SubCatagory, on_delete=models.CASCADE, blank=True)
    sub_cat_name   = models.ForeignKey(SubSubCatagory, on_delete=models.CASCADE, blank=True, null = True)
    brand_name     = models.ForeignKey(Brands, on_delete=models.CASCADE, blank=True, null = True)
    product_name   = models.TextField(max_length=200)
    product_code   = models.CharField(max_length=20, blank=True)
    product_image1 = models.ImageField(upload_to='products', blank=True)
    product_image2 = models.ImageField(upload_to='products', blank=True)
    product_image3 = models.ImageField(upload_to='products', blank=True)
    product_image4 = models.ImageField(upload_to='products', blank=True)
    product_image5 = models.ImageField(upload_to='products', blank=True)
    price          = models.FloatField(default=0)
    regular_price  = models.FloatField(default=0)
    total_sale     = models.IntegerField(default=0)
    add_date       = models.DateField(auto_now_add=True)
    short_features = RichTextField(blank=True)
    description    = RichTextField(blank=True)
    status_types   = (
        ('1',  'In Stock'),
        ('2',  'Out of Stock'),
    )
    stock_status   = models.CharField(max_length=1, choices=status_types)
    stock_quantity = models.IntegerField(default=0)
    ordering       = models.IntegerField(default=0)
    status         = models.BooleanField(default=True)
    feature1_title = models.CharField("Feature One Title", max_length = 50, blank=True)
    feature1       = models.TextField("Feature One Text", blank=True)
    feature2_title = models.CharField("Feature Two Title", max_length = 50, blank=True)
    feature2       = models.TextField("Feature Two Text", blank=True)
    feature3_title = models.CharField("Feature Three Title", max_length = 50, blank=True)
    feature3       = models.TextField("Feature Three Text", blank=True)
    feature4_title = models.CharField("Feature Four Title", max_length = 50, blank=True)
    feature4       = models.TextField("Feature Four Text", blank=True)
    feature5_title = models.CharField("Feature Five Title", max_length = 50, blank=True)
    feature5       = models.TextField("Feature Five Text", blank=True)
    feature6_title = models.CharField("Feature Six Title", max_length = 50, blank=True)
    feature6       = models.TextField("Feature Six Text", blank=True)
    feature7_title = models.CharField("Feature Seven Title", max_length = 50, blank=True)
    feature7       = models.TextField("Feature Seven Text", blank=True)
    feature8_title = models.CharField("Feature Eight Title", max_length = 50, blank=True)
    feature8       = models.TextField("Feature Eight Text", blank=True)
    feature9_title = models.CharField("Feature Nine Title", max_length = 50, blank=True)
    feature9       = models.TextField("Feature Nine Text", blank=True)
    feature10_title = models.CharField("Feature Ten Title", max_length = 50, blank=True)
    feature10       = models.TextField("Feature Ten Text", blank=True)
    feature11_title = models.CharField("Feature Eleven Title", max_length = 50, blank=True)
    feature11       = models.TextField("Feature Twelve Text", blank=True)
    feature12_title = models.CharField("Feature Thirteen Title", max_length = 50, blank=True)
    feature13       = models.TextField("Feature Thirteen Text", blank=True)
    feature14_title = models.CharField("Feature Fourteen Title", max_length = 50, blank=True)
    feature14       = models.TextField("Feature Fourteen Text", blank=True)
    feature15_title = models.CharField("Feature Fifteen Title", max_length = 50, blank=True)
    feature15       = models.TextField("Feature Fifteen Text", blank=True)
    feature16_title = models.CharField("Feature Sixteen Title", max_length = 50, blank=True)
    feature16       = models.TextField("Feature Sixteen Text", blank=True)
    feature17_title = models.CharField("Feature Seventeen Title", max_length = 50, blank=True)
    feature17       = models.TextField("Feature Seventeen Text", blank=True)
    feature18_title = models.CharField("Feature Eighteen Title", max_length = 50, blank=True)
    feature18       = models.TextField("Feature Eighteen Text", blank=True)
    feature19_title = models.CharField("Feature Nineteen Title", max_length = 50, blank=True)
    feature19       = models.TextField("Feature Nineteen Text", blank=True)
    feature20_title = models.CharField("Feature Twenty Title", max_length = 50, blank=True)
    feature20       = models.TextField("Feature Twenty Text", blank=True)
    feature21_title = models.CharField("Feature Twenty One Title", max_length = 50, blank=True)
    feature21       = models.TextField("Feature Twenty One Text", blank=True)
    feature22_title = models.CharField("Feature Twenty Two Title", max_length = 50, blank=True)
    feature22       = models.TextField("Feature Twenty Two Text", blank=True)
    feature23_title = models.CharField("Feature Twenty Three Title", max_length = 50, blank=True)
    feature23       = models.TextField("Feature Twenty Three Text", blank=True)
    feature24_title = models.CharField("Feature Twenty Four Title", max_length = 50, blank=True)
    feature24       = models.TextField("Feature Twenty Four Text", blank=True)
    feature25_title = models.CharField("Feature Twenty Five Title", max_length = 50, blank=True)
    feature25       = models.TextField("Feature Twenty Five Text", blank=True)
    feature26_title = models.CharField("Feature Twenty Six Title", max_length = 50, blank=True)
    feature26       = models.TextField("Feature Twenty Six Text", blank=True)
    feature27_title = models.CharField("Feature Twenty Seven Title", max_length = 50, blank=True)
    feature27       = models.TextField("Feature Twenty Seven Text", blank=True)
    feature28_title = models.CharField("Feature Twenty Eight Title", max_length = 50, blank=True)
    feature28       = models.TextField("Feature Twenty Eight Text", blank=True)
    feature29_title = models.CharField("Feature Twenty Nine Title", max_length = 50, blank=True)
    feature29       = models.TextField("Feature Twenty Nine Text", blank=True)
    feature30_title = models.CharField("Feature Thirty Title", max_length = 50, blank=True)
    feature30       = models.TextField("Feature Thirty Text", blank=True)

    def url(self):
        return os.path.join('/static/shop/media/products/', os.path.basename(str(self.product_image1)))

    def photo(self):
        return mark_safe('<img src = "{}" width="60" height = "60"/>'.format(self.url()))

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'All Products'

class AddToCart(models.Model):
    product_name  = models.ForeignKey(Products, on_delete=models.CASCADE)
    ip_address    = models.CharField(max_length=50)
    mac_address   = models.CharField(max_length=50)
    qt_price      = models.IntegerField(default = 0)
    quantity      = models.IntegerField(default = 1)
    total_price   = models.IntegerField(default = 0)
    cart_date     = models.DateTimeField(auto_now_add = True)
    status        = models.BooleanField(default=1)
    def __str__(self):
        return str(self.product_name)
    
    class Meta:
        verbose_name = 'Add To Cart'
        verbose_name_plural = 'Cart List'

class Wishlist(models.Model):
    product_name  = models.ForeignKey(Products, on_delete=models.CASCADE)
    ip_address    = models.CharField(max_length=50)
    mac_address   = models.CharField(max_length=50)
    total_price   = models.IntegerField(default = 0)
    wish_date     = models.DateTimeField(auto_now_add = True)
    status        = models.BooleanField(default=1)
    def __str__(self):
        return str(self.product_name)
    
    class Meta:
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'

class UserRegistration(models.Model):
    user_name        = models.CharField(max_length=100, blank=True)
    user_email       = models.EmailField(unique = True)
    user_password    = models.CharField(max_length=100)
    user_mobile      = models.CharField(max_length=15)
    address          = models.TextField(blank=True)
    status           = models.BooleanField(default=True)

    def __str__(self):
        return self.user_name
    
    class Meta:
        verbose_name = 'User Registration'
        verbose_name_plural = 'Users Registration'

class Branches(models.Model):
    branch_name      = models.CharField(max_length=100)
    proprietor_name  = models.CharField(max_length=50, blank=True)
    email1           = models.EmailField(blank=True)
    email2           = models.EmailField(blank=True)
    mobile1          = models.CharField(max_length=15)
    mobile2          = models.CharField(max_length=15, blank=True)
    off_day          = models.CharField(max_length=15, blank=True)
    address          = models.TextField(blank=True)
    status           = models.BooleanField(default=True)

    def __str__(self):
        return self.branch_name
    
    class Meta:
        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'

class ContactUs(models.Model):
    customer_name = models.CharField(max_length=30)
    email_address = models.EmailField(max_length=70)
    subject       = models.CharField(max_length=150)
    message       = models.TextField()
    ip_address    = models.CharField(max_length=20, blank=True)
    mobile        = models.CharField(max_length=15)
    email_date    = models.DateTimeField(auto_now_add=True)
    seen_status   = models.BooleanField(default=False)

    def __str__(self):
        return self.customer_name

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'

class AboutUs(models.Model):
    title            = models.CharField(max_length = 200, blank = True)
    description      = RichTextField()
    meta_description = models.TextField(blank = True)
    meta_keywords    = models.TextField(blank = True)
    meta_title       = models.TextField(blank = True)
    status           = models.BooleanField(default = True)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'

class Emi(models.Model):
    title            = models.CharField(max_length = 200, blank = True)
    description      = RichTextField()
    meta_description = models.TextField(blank = True)
    meta_keywords    = models.TextField(blank = True)
    meta_title       = models.TextField(blank = True)
    status           = models.BooleanField(default = True)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = 'EMI'
        verbose_name_plural = 'EMI'

class Warranty(models.Model):
    title            = models.CharField(max_length = 200, blank = True)
    description      = RichTextField()
    meta_description = models.TextField(blank = True)
    meta_keywords    = models.TextField(blank = True)
    meta_title       = models.TextField(blank = True)
    status           = models.BooleanField(default = True)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = 'Warranty'
        verbose_name_plural = 'Warranties'

class PaymentMethod(models.Model):
    title            = models.CharField(max_length = 200, blank = True)
    description      = RichTextField()
    meta_description = models.TextField(blank = True)
    meta_keywords    = models.TextField(blank = True)
    meta_title       = models.TextField(blank = True)
    status           = models.BooleanField(default = True)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = 'Payment Method'
        verbose_name_plural = 'Payment Methods'

class TermsConditions(models.Model):
    title            = models.CharField(max_length = 200, blank = True)
    description      = RichTextField()
    meta_description = models.TextField(blank = True)
    meta_keywords    = models.TextField(blank = True)
    meta_title       = models.TextField(blank = True)
    status           = models.BooleanField(default = True)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = 'Terms & Condition'
        verbose_name_plural = 'Terms & Conditions'

class ReturnRefundPolicy(models.Model):
    title            = models.CharField(max_length = 200, blank = True)
    description      = RichTextField()
    meta_description = models.TextField(blank = True)
    meta_keywords    = models.TextField(blank = True)
    meta_title       = models.TextField(blank = True)
    status           = models.BooleanField(default = True)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = 'Return Refund Policy'
        verbose_name_plural = 'Return Refund Policy'

class PrivacyPolicy(models.Model):
    title            = models.CharField(max_length = 200, blank = True)
    description      = RichTextField()
    meta_description = models.TextField(blank = True)
    meta_keywords    = models.TextField(blank = True)
    meta_title       = models.TextField(blank = True)
    status           = models.BooleanField(default = True)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = 'Privacy Policy'
        verbose_name_plural = 'Privacy Policy'

class OfferProduct(models.Model):
    product          = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True)
    title            = models.CharField(max_length = 200, blank = True)
    description      = RichTextField()
    thumbnail_image  = models.ImageField(upload_to='thumbnail_image', blank=True)
    meta_description = models.TextField(blank = True)
    meta_keywords    = models.TextField(blank = True)
    meta_title       = models.TextField(blank = True)
    status           = models.BooleanField(default = True)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = 'Offer Product'
        verbose_name_plural = 'Offer Products'


class SeoContent(models.Model):
    index_meta_title            = models.TextField(blank = True)
    index_meta_description      = models.TextField(blank = True)
    index_meta_keywords         = models.TextField(blank = True)
    contact_us_title            = models.TextField(blank=True)
    contact_us_description      = models.TextField(blank=True)
    contact_us_keywords         = models.TextField(blank=True)
    offer_product_title         = models.TextField(blank=True)
    offer_product_description   = models.TextField(blank=True)
    offer_product_keywords      = models.TextField(blank=True)
    faq_title                   = models.TextField(blank=True)
    faq_description             = models.TextField(blank=True)
    faq_keywords                = models.TextField(blank=True)
    login_title                 = models.TextField(blank=True)
    login_description           = models.TextField(blank=True)
    login_keywords              = models.TextField(blank=True)
    reg_title                   = models.TextField(blank=True)
    reg_description             = models.TextField(blank=True)
    reg_keywords                = models.TextField(blank=True)
    fogt_title                  = models.TextField(blank=True)
    fogt_description            = models.TextField(blank=True)
    fogt_keywords               = models.TextField(blank=True)
    status                      = models.BooleanField(default=True)

    def __str__(self):
        return self.index_meta_title   

    class Meta:
        verbose_name = 'Seo Content'
        verbose_name_plural = 'Seo Contentes'
