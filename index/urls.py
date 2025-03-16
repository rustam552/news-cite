from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'index'
urlpatterns=[
    path('', views.home_page),
    path('category/<int:pk>', views.category_page, name='category_page'),
    path('news/<int:pk>', views.news_page, name='news_page'),
    path('register', views.Register.as_view()),
    path('search', views.search_product)
]