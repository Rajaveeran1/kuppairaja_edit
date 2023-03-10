# Generated by Django 4.1 on 2023-03-04 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('buyer', '0004_fcategory_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productdetails', models.TextField(default='', max_length=1000, null=True)),
                ('kilograms', models.IntegerField(default='')),
                ('price', models.FloatField(default='')),
                ('phoneno', models.CharField(default='', max_length=10)),
                ('address', models.TextField(blank=True, default='')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='', max_length=25)),
                ('favourite', models.BooleanField(default=False)),
                ('likes', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='buyer.category')),
                ('item', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='buyer.subcategory')),
                ('userid', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MultipleImages',
            fields=[
                ('scrapimageid', models.AutoField(primary_key=True, serialize=False)),
                ('scrapimage', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('scrapid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='seller.product')),
            ],
        ),
    ]
