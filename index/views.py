from django.shortcuts import render, redirect
from .models import News, NewsCategory
from . forms import RegForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.views import View
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
    category = NewsCategory.objects.get(id=pk)
    news = News.objects.filter(category=category).order_by('-created_at')
    categories = NewsCategory.objects.all()
    context = {
        'news': news,
        'category': category,
        'categories': categories,
    }
    return render(request, 'category.html', context)

def news_page(request, pk):
    news_item = News.objects.get(id=pk)
    # Определяем шаблон в зависимости от категории
    category_name = news_item.category.name.lower()
    if category_name == 'technologies':
        template_name = 'technologies.html'
    elif category_name == 'animals':
        template_name = 'animals.html'
    elif category_name == 'politics':
        template_name = 'politics.html'
    else:
        template_name = 'news_detail.html'  # Если категория неизвестна, используем общий шаблон

    context = {
        'news_item': news_item
    }
    return render(request, template_name, context)

#Регистрация
class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {'form': RegForm}
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegForm(request.POST)
        print(form)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password2')

            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)
            user.save()

            login(request, user)
            return redirect('/')

# Поиск продукта
def search_product(request):
    if request.method=='POST':
        get_product = request.POST.get('search_product')

        searched_news = News.objects.filter(title__iregex=get_product)
        if searched_news.exists():
            context={'news': searched_news}
            return render(request, 'result,html', context)
        else:
            return redirect('/')

# Log out
def logout_view(request):
    logout(request)
    return redirect('/')

