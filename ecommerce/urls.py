from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Computer Care Technology Admin Panel"
admin.site.site_title = "Computer Care Technology Super Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shop.urls')),
    path('/',include('shop.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
