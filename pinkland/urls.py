"""pinkland URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pinkland.views import HomePageView,ProductPageView, ContactUsPageView, AboutUsPageView, ProductDetail ,ProductList
from django.conf import settings
from django.conf.urls.static import static
import logging

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('product/', ProductPageView.as_view(), name='product'),
    path('product_list/', ProductList.as_view()),
    path('product_detail/<int:id>', ProductDetail.as_view(),name='product_detail'),
    # Type . Part . Function
    # path('product/<str:ptype>/<str:ppart>/<str:pfunc>',ProductPageView.filterProduct, name='product_filtered'),
    # path('product/<int:id>/', ProductDetailPageView.as_view(), name='product_detail'),
    path('contactus/', ContactUsPageView.as_view(), name='contactus'),
    path('aboutus/', AboutUsPageView.as_view(), name='aboutus'), 
] 

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
