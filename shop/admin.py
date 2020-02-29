from django.contrib import admin
from . import models
from django.utils.html import format_html

class CompanyInfoAdmin(admin.ModelAdmin):
    list_display    = ['com_name','status']
    search_fields   = ['com_name','status']
    list_filter     = ['status']

class SubscriberNewslatterAdmin(admin.ModelAdmin):
    list_display    = ['subscriber_email']
    search_fields   = ['subscriber_email']

class SliderInfoAdmin(admin.ModelAdmin):
    list_display    = ['slider_name']
    search_fields   = ['slider_name']

class CatagoryAdmin(admin.ModelAdmin):
    list_display    = ['cat_name','status']
    search_fields   = ['cat_name']
    
class BrandsAdmin(admin.ModelAdmin):
    list_display    = ['brand_name']
    search_fields   = ['brand_name']
    
class SubCatagoryAdmin(admin.ModelAdmin):
    list_display    = ['cat_name','sub_category']
    list_filter     = ['cat_name','status']

class SubSubCatagoryAdmin(admin.ModelAdmin):
    list_display    = ['cat_name','sub_category']
    list_filter     = ['cat_name','status']

class ProductsAdmin(admin.ModelAdmin):
    list_display    = ['cat_name','sub_cat_name','brand_name']
    list_filter     = ['cat_name','sub_cat_name','brand_name','status']

class UserRegistrationAdmin(admin.ModelAdmin):
    list_display    = ['user_name','user_email','status']
    search_fields   = ['user_name','user_email','status']
    list_filter     = ['user_name','user_email','status']

class BranchesAdmin(admin.ModelAdmin):
    list_display    = ['branch_name','proprietor_name','status']
    search_fields   = ['branch_name','proprietor_name','status']
    list_filter     = ['branch_name','proprietor_name','status']

class ContactUsAdmin(admin.ModelAdmin):
    list_display    = ['customer_name','email_address','ip_address','seen_status']
    search_fields   = ['customer_name','email_address','seen_status']
    list_filter     = ['customer_name','email_address','seen_status']

class AboutUsAdmin(admin.ModelAdmin):
    list_display    = ['meta_title','status']
    search_fields   = ['title','status']
    list_filter     = ['title','status']

class EmiAdmin(admin.ModelAdmin):
    list_display    = ['meta_title','status']
    search_fields   = ['title','status']
    list_filter     = ['title','status']

class WarrantyAdmin(admin.ModelAdmin):
    list_display    = ['meta_title','status']
    search_fields   = ['title','status']
    list_filter     = ['title','status']

class PaymentMethodAdmin(admin.ModelAdmin):
    list_display    = ['meta_title','status']
    search_fields   = ['title','status']
    list_filter     = ['title','status']

class TermsConditionsAdmin(admin.ModelAdmin):
    list_display    = ['meta_title','status']
    search_fields   = ['title','status']
    list_filter     = ['title','status']

class ReturnRefundPolicyAdmin(admin.ModelAdmin):
    list_display    = ['meta_title','status']
    search_fields   = ['title','status']
    list_filter     = ['title','status']

class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display    = ['meta_title','status']
    search_fields   = ['title','status']
    list_filter     = ['title','status']

class AddToCartAdmin(admin.ModelAdmin):
    list_display    = ['product_name','quantity','total_price','status']
    search_fields   = ['product_name__product_name','status']
    list_filter     = ['cart_date','status']

class WishlistAdmin(admin.ModelAdmin):
    list_display    = ['product_name','status']
    search_fields   = ['product_name__product_name','status']
    list_filter     = ['wish_date','status']

admin.site.register(models.CompanyInfo, CompanyInfoAdmin)
admin.site.register(models.SubscriberNewslatter, SubscriberNewslatterAdmin)
admin.site.register(models.SliderInfo, SliderInfoAdmin)
admin.site.register(models.Catagory, CatagoryAdmin)
admin.site.register(models.Brands, BrandsAdmin)
admin.site.register(models.SubCatagory, SubCatagoryAdmin)
admin.site.register(models.SubSubCatagory, SubSubCatagoryAdmin)
admin.site.register(models.Products, ProductsAdmin)
admin.site.register(models.UserRegistration, UserRegistrationAdmin)
admin.site.register(models.Branches, BranchesAdmin)
admin.site.register(models.ContactUs, ContactUsAdmin)
admin.site.register(models.AboutUs, AboutUsAdmin)
admin.site.register(models.Emi, EmiAdmin)
admin.site.register(models.Warranty, WarrantyAdmin)
admin.site.register(models.PaymentMethod, PaymentMethodAdmin)
admin.site.register(models.TermsConditions, TermsConditionsAdmin)
admin.site.register(models.ReturnRefundPolicy, ReturnRefundPolicyAdmin)
admin.site.register(models.PrivacyPolicy, PrivacyPolicyAdmin)
admin.site.register(models.SeoContent)
admin.site.register(models.OfferProduct)
admin.site.register(models.AddToCart, AddToCartAdmin)
admin.site.register(models.Wishlist,WishlistAdmin)
