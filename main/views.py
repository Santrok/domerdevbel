from datetime import datetime, date, timedelta

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView

from .forms import PhotoForm
from .models import Advertisement, Region, Category
from .serializers import (RegionSerializer,
                          CategorySerializer,
                          AdvertisementSerializer)
from .utils import sorted_by_number, variables_for_paginator

sort_for_paginator = 3


# Create your views here.

def get_main_page(request):
    global sort_for_paginator
    advertisement_queryset = Advertisement.objects.filter(is_active=True,
                                                          moderation=True).order_by("-date_of_create")
    category_queryset = Category.objects.filter(level=0).annotate(num_adver=Count('advertisement'))
    if request.GET.get('sort'):
        sort_for_paginator = sorted_by_number(request.GET.get('sort'))
    page_obj = variables_for_paginator(advertisement_queryset, sort_for_paginator, request.GET.get('page'))

    context = {
        "adver": advertisement_queryset,
        "category": category_queryset,
        "page_obj": page_obj,

    }

    return render(request, 'param1.html', context)


def get_main_page2(request):
    global sort_for_paginator
    advertisement_queryset = Advertisement.objects.filter(is_active=True,
                                                          moderation=True).order_by("-date_of_create")
    category_queryset = Category.objects.filter(level=0).annotate(num_adver=Count('advertisement'))
    if request.GET.get('sort'):
        sort_for_paginator = sorted_by_number(request.GET.get('sort'))
    page_obj = variables_for_paginator(advertisement_queryset, sort_for_paginator, request.GET.get('page'))


    context = {
        "adver": advertisement_queryset,
        "category": category_queryset,
        "page_obj": page_obj,

    }

    return render(request, 'param2.html', context)


def get_main_page3(request):
    advertisement_queryset = Advertisement.objects.filter(is_active=True,
                                                          moderation=True).order_by("-date_of_create")

    context = {
        "adver": advertisement_queryset,

    }
    return render(request, 'param3.html', context)


def get_advertisement_by_category(request, category_slug):
    global sort_for_paginator
    if request.GET.get('sort'):
        sort_for_paginator = sorted_by_number(request.GET.get('sort'))
    category_queryset = Category.objects.filter(level=0).annotate(num_adver=Count('advertisement'))
    category = get_object_or_404(category_queryset, slug=category_slug)
    advertisement_queryset = Advertisement.objects.filter(category=category.id, is_active=True,
                                                          moderation=True).order_by("-date_of_create")

    page_obj = variables_for_paginator(advertisement_queryset, sort_for_paginator, request.GET.get('page'))

    context = {
        "adver": advertisement_queryset,
        "category": category_queryset,
        "page_obj": page_obj,

    }

    return render(request, 'param1.html', context)


def get_advertisement_by_category2(request, category_slug):
    global sort_for_paginator
    if request.GET.get('sort'):
        sort_for_paginator = sorted_by_number(request.GET.get('sort'))
    category_queryset = Category.objects.filter(level=0).annotate(num_adver=Count('advertisement'))
    category = get_object_or_404(category_queryset, slug=category_slug)
    advertisement_queryset = Advertisement.objects.filter(category=category.id, is_active=True,
                                                          moderation=True).order_by("-date_of_create")

    page_obj = variables_for_paginator(advertisement_queryset, sort_for_paginator, request.GET.get('page'))

    context = {
        "adver": advertisement_queryset,
        "category": category_queryset,
        "page_obj": page_obj,

    }

    return render(request, 'param2.html', context)


# def get_main_page(request):
#     advertisement_queryset = Advertisement.objects.filter(is_active=True,
#                                                           moderation=True).order_by("-date_of_create")[:7]
#     form = PhotoForm
#     if request.method == "POST":
#         form = PhotoForm(request.POST, request.FILES)
#         if form.is_valid():
#             print(form.cleaned_data)
#     context = {
#         "adver": advertisement_queryset,
#         "form": form,
#
#     }
#     return render(request, 'main.html', context)


class RegionAPIView(ListAPIView):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()


class CategoryAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class AdvertisementAPIView(ListAPIView):
    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.filter(is_active=True,
                                            moderation=True).order_by("-date_of_create")[:7]


def fetch_zapros(request):
    return render(request, 'fetch.html')