from time import time

from django.shortcuts import render, redirect
from .forms import Clients_phone
from .models import Client



def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html', {'ph': 'static/images/dj-neo1.img'})


def contact(request):
    if request.method == 'POST':

        form = Clients_phone(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('thanks')
    else:
        form = Clients_phone()
    return render(request, 'contact.html', {'form': form})



def work(request):
    return render(request, 'work.html')


def secret_master(request):
    return render(request, 'blog.html')


def thanks(request):
    return render(request, 'thanks.html')


def work_single(request):
    return render(request, 'work-single.html')

def blog(request):
    return render(request, 'blog.html')


def blog_single(request):
    return render(request, 'blog-single.html')

