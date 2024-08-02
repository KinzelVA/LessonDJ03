from django.shortcuts import render
from .models import News

def home(request):
    return render(request, 'news/home.html')

def news_list(request):
    news = News.objects.all()
    return render(request, 'news/news_list.html', {'news': news})

def about(request):
    return render(request, 'news/about.html')

