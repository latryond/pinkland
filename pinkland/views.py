# from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.views import View


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        title = "asdfasdf"
        context = {
            'title':title
        }
        return render(request, 'index.html', context)