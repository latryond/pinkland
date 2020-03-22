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
        product = Product.objects.all()
        paginator = Paginator(product, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # product_categ_choice = body_part_choice = func_choice = ["全部"]
        # product_categ_choice = body_part_choice = func_choice = ["all"]
        # for cc in Product.category_choice:
        #     product_categ_choice.append(cc[1])
        # for bc in Product.body_part_choice:
        #     body_part_choice.append(bc[1])
        # for fc in Product.func_choice:
        #     func_choice.append(fc[1])
        
        context = {
            'products': product,
            'types': Product.category_choice,
            'parts': Product.body_part_choice,
            'functions': Product.func_choice,
            'page_obj': page_obj,
        }
        return render(request, 'product.html', context)
    def filterProduct(self, request, ptype, ppart, pfunc):
        logging.error(ptype+"  "+ppart+"  "+pfunc)

    


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
