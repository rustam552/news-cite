from django.shortcuts import render
from .models import News, NewsCategory
# Create your views here.
def home_page(request):
    news = News.objects.all().order_by('-created_at')
    categories = NewsCategory.objects.all()

    context = {
        'news': news,
        'categories': categories,
    }
    return render(request, "home.html",context)

def category_page(request, pk):
    news = News.objects.all().order_by('-created_at')
    categories = NewsCategory.objects.get(id=pk)
    context = {
        'news': news,
        'categories': categories,
    }
    return render(request, 'politics.html', context)

def news_page(request, pk):
    news = News.objects.all().order_by('-created_at')
    context = {
        'news': news
    }
    return render(request, 'politics.html', context)
