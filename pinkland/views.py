# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
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
        paginator = Paginator(p, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        p_type = ["全部","粉水晶","紫水晶","黃水晶","超級七","金髮晶","綠幽靈","月亮石","拉長石","虎眼石","白水晶","海藍寶","摩根石","紅紋石","草莓石","白幽靈","太陽石","瑪瑙"]
        p_part = ["全部","手鏈", "吊墜", "戒指", "耳環", "擺設", "設計手鏈", "項鏈", "鐲形手鏈"]
        p_function=["全部","事業","人緣","健康","情緒","減壓","愛情","淨化","財運","辟邪","防小人"]
        
        context = {
            'products': p,
            'types': p_type,
            'parts': p_part,
            'functions': p_function,
            'page_obj': page_obj,
        }
        return render(request, 'product.html', context)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filtered_type"] = self.pd_type
        context["filtered_part"] = self.pd_part
        return context

    def get_queryset(self):
        logging.error("get_queryset")
        self.type = get_object_or_404(
            Product, type=self.kwargs['pd_type'], part=self.kwargs['pd_part'], func=self.kwargs['pd_func'])
        return Product.objects.filter(type=self.type)
    


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


class ProductDetailPageView(View):
    def get(self, request, *args, **kwargs):
        title = "ProductDetail"
        context = {
            'title': title
        }
        return render(request, 'product_detail.html', context)
