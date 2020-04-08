# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from .models import Product, ProductImages, Poster, ProductMaterial, ProductCategory, ProductFunction
from datetime import timedelta
import requests 



class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_product'] = Product.objects.all().order_by("-date_create")[:3]
        context['posters'] = Poster.objects.all()
        context['igposts'] = fetchInstragramPost()
        return context

class ProductList(ListView):
    template_name = "product_list.html"
    model = Product 
    paginate_by = 9
    def get_queryset(self):
        if  'filter' in self.kwargs:
            filter_field = self.kwargs['filter']
            filter_value = self.kwargs['value']
            search_type = 'exact'
            filter = filter_field + '__' + search_type
            info = Product.objects.filter(**{ filter: filter_value })
            return info
        return Product.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        context['materials'] = ProductMaterial.objects.all()
        context['categ'] = ProductCategory.objects.all()
        context['functions'] = ProductFunction.objects.all()
        return context

class ProductDetail(DetailView):
    model = Product
    template_name = "product_detail.html"
    def get_object(self, **kwargs):
        p = Product.objects.get(id=self.kwargs['id'])
        p.images =  ProductImages.objects.filter(p_id=self.kwargs['id'])
        return p
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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

def fetchInstragramPost():
    IG_APP_ID = 260032918354934
    ACCESS_TOKEN = refreshInstegramToken()
    payload = {
        'fields': 'id,media_type,media_url,caption',
        'access_token': ACCESS_TOKEN
        }
    request = requests.get('https://graph.instagram.com/me/media', params=payload)
    json = request.json()
    return json

def refreshInstegramToken():
    payload = {
        'grant_type': 'ig_refresh_token',
        'access_token': 'IGQVJWV20xWERaUU1BWTVkdGJWcE4xcnNEUVB4ZAExITkdILXIza2lXMG5YUG00RzVXb3FmVkpSZAGd6QTlmSHhGbnduSEJnRXNTNXdDS3B4TEhKNDkxdlBrQXUyRTM0SlJITmdFOUVB'
        }
    r = requests.get('https://graph.instagram.com/refresh_access_token', params=payload)
    request_dict = r.json()
    return request_dict['access_token']