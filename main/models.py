from django.contrib.auth.models import User
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Region(MPTTModel):
    REGION_1 = 'Область'
    REGION_2 = 'Город'

    region_choices = [
        (REGION_1, 'Область'),
        (REGION_2, 'Город')
    ]

    region = models.CharField(max_length=100)
    type = models.CharField(choices=region_choices, max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True,
                            blank=True, related_name='children')
    slug = models.SlugField('url', max_length=50, unique=True)

    def __str__(self):
        return self.region


class Category(MPTTModel):
    CATEGORY_1 = 'category_1'
    CATEGORY_2 = 'category_2'
    CATEGORY_3 = 'category_3'
    CATEGORY_4 = 'category_4'

    type_choices = [
        (CATEGORY_1, ("category_1")),
        (CATEGORY_2, ("category_2")),
        (CATEGORY_3, ("category_3")),
        (CATEGORY_4, ("category_4")),
    ]
    title = models.CharField(max_length=100)
    type = models.CharField(choices=type_choices, max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True,
                            blank=True, related_name='children')
    slug = models.SlugField('url', max_length=50, unique=True)

    def __str__(self):
        return self.title


class Advertisement(models.Model):
    BEARER_CHOICES = [
        (1, 'Компания'),
        (0, 'Частное лицо')
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    bearer = models.IntegerField(choices=BEARER_CHOICES)
    city = models.ForeignKey('Region',
                             on_delete=models.PROTECT)
    previous_image = models.ImageField(upload_to="media",
                                       default='/media/no_image.jpg')
    images = models.OneToOneField('Gallery',
                                  on_delete=models.CASCADE,
                                  blank=True, null=True)
    date_of_create = models.DateTimeField(auto_now_add=True)
    moderation = models.BooleanField(default=False)
    contact_name = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    video_link = models.CharField(max_length=300, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    slug = models.SlugField('url', max_length=50, unique=True)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    name = models.CharField(max_length=50)
    photos = models.ManyToManyField('Photo')
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField('url', max_length=50, unique=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='media')
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField('url', max_length=50, unique=True)
    advertisement = models.ForeignKey("Advertisement",
                                      on_delete=models.CASCADE)

    def __str__(self):
        return self.name
