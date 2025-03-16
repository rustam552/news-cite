from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_photo',
            field=models.ImageField(blank=True, null=True, upload_to='news_photos/', verbose_name='Фото новости'),
            preserve_default=False,
        ),
    ]