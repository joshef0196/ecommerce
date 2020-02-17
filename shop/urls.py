from shop import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('contact-us/', views.contact),
    path('about-us/', views.about_us),
    path('emi-terms/', views.emi),
    path('warranty-policy/', views.warranty),
    path('payment-method/', views.payment_method),
    path('terms-and-conditions/', views.terms_conditions),
    path('refund-policy/', views.return_refund_policy),
    path('privacy/', views.privacy_policy),
    path('offers/', views.offers),
    path('faq/', views.faq),
    path('wishlist/', views.wishlist),
    path('cart-list/', views.cart_list),
    path('checkout/', views.checkout),
    path('order-success/', views.order_complete),
    path('single/', views.single_product),
    # path('<str:cat_name>/<str:sub_cat>/', views.products_cat),
    path('test/', views.products_cat),
]
