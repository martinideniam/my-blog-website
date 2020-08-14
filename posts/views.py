from django.shortcuts import render
from .models import post
from django.views.generic import ListView

# Create your views here.


def homePage(request):
    template_name = "posts/home.html"
    context = {'posts': post.objects.all()}
    return render(request, template_name, context)
