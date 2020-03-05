# from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Product, ProductImage
import logging 
class HomePageView(View):
    def get(self, request, *args, **kwargs):
        title = "asdfasdf"
        context = {
            'title':title
        }
        return render(request, 'index.html', context)


class ProductPageView(View):
    def get(self, request, *args, **kwargs):
        title = "Product"
        p = Product.objects.all()
        p_type = ["粉水晶","紫水晶","黃水晶","超級七","金髮晶","綠幽靈","月亮石","拉長石","虎眼石","白水晶","海藍寶","摩根石","紅紋石","草莓石","白幽靈","太陽石","瑪瑙"]
        p_part = ["手鏈","吊墜","戒指","耳環","擺設","設計手鏈","項鏈","鐲形手鏈"]
        p_function=["事業","人緣","健康","情緒","減壓","愛情","淨化","財運","辟邪","防小人"]
        context = {
            'products': p,
            'types': p_type,
            'parts': p_part,
            'functions': p_function,
        }
        return render(request, 'product.html', context)


class ContactUsPageView(View):
    def get(self, request, *args, **kwargs):
        title = "ContactUs"
        context = {
            'title': title
        }
        return render(request, 'contactus.html', context)


class AboutUsPageView(View):
    def get(self, request, *args, **kwargs):
        title = "AboutUs"
        context = {
            'title': title
        }
        return render(request, 'aboutus.html', context)
