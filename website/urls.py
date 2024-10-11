
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



admin.site.site_header="Blogs Admin Panel"
# admin.site.site_title=" Admin Login"
admin.site.site_url="Blog-Admin-Panel"
urlpatterns = [
    path('', views.home,name='home' ),
    path('home', views.home,name='home' ),
    path('category', views.category,name='category' ),
    path('post/<int:sno>/<str:slug>', views.page,name='page' ),
    path('contact',views.contact,name='contact' ),
    path('blog', views.blog ,name='blog'),
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
