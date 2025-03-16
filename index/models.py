from django.db import models

# Create your models here.
class NewsCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    created_at= models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Категория новостей'
        verbose_name_plural = 'Категории новостей'

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Основной текст')
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, verbose_name='Категория')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    news_photo = models.ImageField(upload_to='news_photos/', null=True, blank=True, verbose_name='Фото новости')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
