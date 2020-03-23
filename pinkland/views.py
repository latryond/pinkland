# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
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
        
        context = {
            'products': product,
            'types': Product.category_choice,
            'parts': Product.body_part_choice,
            'functions': Product.func_choice,
            'page_obj': page_obj,
        }
        return render(request, 'product.html', context)

class ProductList(ListView):
    template_name = "product_list.html"
    model = Product 
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['materials'] = Product.category_choice
        context['parts'] = Product.body_part_choice
        context['functions'] = Product.func_choice
        return context

class ProductDetail(DetailView):
    model = Product
    template_name = "product_detail.html"
    def get_object(self, **kwargs):
        p = Product.objects.get(id=self.kwargs['id'])
        p.images =  ProductImage.objects.filter(product_id=self.kwargs['id'])
        return p
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['materials'] = Product.category_choice
        context['parts'] = Product.body_part_choice
        context['functions'] = Product.func_choice
        return context


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



