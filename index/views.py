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



