# Generated by Django 5.0.1 on 2024-01-18 15:59

import django.db.models.deletion
import mptt.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True, verbose_name='url')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('category_1', 'category_1'), ('category_2', 'category_2'), ('category_3', 'category_3'), ('category_4', 'category_4')], max_length=50)),
                ('slug', models.SlugField(unique=True, verbose_name='url')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='main.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.TextField(blank=True, null=True)),
                ('bearer', models.IntegerField(choices=[(1, 'Компания'), (0, 'Частное лицо')])),
                ('previous_image', models.ImageField(default='/media/no_image.jpg', upload_to='media')),
                ('date_of_create', models.DateTimeField(auto_now_add=True)),
                ('moderation', models.BooleanField(default=False)),
                ('contact_name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.PositiveIntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('video_link', models.CharField(blank=True, max_length=300, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(unique=True, verbose_name='url')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
                ('images', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.gallery')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='media')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True, verbose_name='url')),
                ('advertisement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.advertisement')),
            ],
        ),
        migrations.AddField(
            model_name='gallery',
            name='photos',
            field=models.ManyToManyField(to='main.photo'),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('Область', 'Область'), ('Город', 'Город')], max_length=50)),
                ('slug', models.SlugField(unique=True, verbose_name='url')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='main.region')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='advertisement',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.region'),
        ),
    ]
