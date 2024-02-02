from datetime import datetime, date, timedelta

from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count, Sum
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView

from .forms import PhotoForm
from .models import Advertisement, Region, Category
from .serializers import (RegionSerializer,
                          CategorySerializer,
                          AdvertisementSerializer)
from .utils import sorted_by_number, variables_for_paginator, sorted_by_date_or_price, sorted_by


# Create your views here.

def get_main_page(request):
    order_by = sorted_by(request.COOKIES.get('sorted_by'))
    sort_for_paginator = sorted_by_number(request.COOKIES.get('sort'))
    state_sort_by_date = request.COOKIES.get('date', 0)

    if request.GET.get('date') or request.GET.get('price'):
        state_sort_by_date, order_by = sorted_by_date_or_price(request.GET)
    if request.GET.get('sort'):
        sort_for_paginator = sorted_by_number(request.GET.get('sort'))

    advertisement_queryset = Advertisement.objects.filter(is_active=True,
                                                          moderation=True).select_related(
        'category', 'city').order_by(order_by)
    category_queryset = Category.objects.filter(level=0).annotate(num_adver=Count('advertisement'))

    page_obj = variables_for_paginator(advertisement_queryset, request.GET.get('page'), sort_for_paginator)

    context = {
        "adver": advertisement_queryset,
        "category": category_queryset,
        "page_obj": page_obj,
        'date': state_sort_by_date,
    }

    response = render(request, 'param1.html', context)
    response.set_cookie('sort', sort_for_paginator)
    response.set_cookie('date', state_sort_by_date)
    response.set_cookie('sorted_by', order_by)

    return response


def get_advertisement_by_category(request, category_slug):
    order_by = sorted_by(request.COOKIES.get('sorted_by'))
    sort_for_paginator = sorted_by_number(request.COOKIES.get('sort'))
    state_sort_by_date = request.COOKIES.get('date', 0)

    if request.GET.get('date') or request.GET.get('price'):
        state_sort_by_date, order_by = sorted_by_date_or_price(request.GET)
    if request.GET.get('sort'):
        sort_for_paginator = sorted_by_number(request.GET.get('sort'))

    category_queryset = Category.objects.annotate(num_adver=Count('advertisement'))
    category = get_object_or_404(category_queryset.filter(level=0), slug=category_slug)
    cat = category_queryset.filter(level=0)
    # category_sum = cat.node.is_root_node()
    print(dir(cat))
    # print(category_sum)
    # print(category_sum)
    print(cat)

    for i in category_queryset:
        print(i.get_root())
    # #     print(i.advertisement_set.all())
    #     sam = i.get_descendants(include_self=False)
    #     print(sam)
    #     for z in sam:
    #         for x in z.advertisement_set.all():
    #             print(x)

    # roots = Category.objects.add_related_count(Category.objects.root_nodes(), Advertisement, 'category', 'num_adver', cumulative=True)
    # print(roots)




    # x = category.get_descendants().annotate(num_adver=Count('advertisement'))
    # print(x.count())
    advertisement_queryset = Advertisement.objects.filter(category__tree_id=category.id, is_active=True,
                                                          moderation=True).select_related(
        'category', 'city').order_by(order_by)
    # print(advertisement_queryset[0].category_id)
    page_obj = variables_for_paginator(advertisement_queryset, request.GET.get('page'), sort_for_paginator)

    context = {
        "adver": advertisement_queryset,
        "category": category_queryset,
        "page_obj": page_obj,
        'date': state_sort_by_date,
    }

    response = render(request, 'param1.html', context)
    response.set_cookie('sort', sort_for_paginator)
    response.set_cookie('date', state_sort_by_date)
    response.set_cookie('sorted_by', order_by)

    return response



def get_main_page2(request):
    order_by = sorted_by(request.COOKIES.get('sorted_by'))
    sort_for_paginator = sorted_by_number(request.COOKIES.get('sort'))
    state_sort_by_date = request.COOKIES.get('date', 0)

    if request.GET.get('date') or request.GET.get('price'):
        state_sort_by_date, order_by = sorted_by_date_or_price(request.GET)
    if request.GET.get('sort'):
        sort_for_paginator = sorted_by_number(request.GET.get('sort'))
    advertisement_queryset = Advertisement.objects.filter(is_active=True,
                                                          moderation=True).select_related(
        'category', 'city').order_by(order_by)
    category_queryset = Category.objects.filter(level=0).annotate(num_adver=Count('advertisement'))
    page_obj = variables_for_paginator(advertisement_queryset, request.GET.get('page'), sort_for_paginator)

    context = {
        "adver": advertisement_queryset,
        "category": category_queryset,
        "page_obj": page_obj,
        'date': state_sort_by_date,
    }

    response = render(request, 'param2.html', context)
    response.set_cookie('sort', sort_for_paginator)
    response.set_cookie('date', state_sort_by_date)
    response.set_cookie('sorted_by', order_by)

    return response




def get_advertisement_by_category2(request, category_slug):
    order_by = sorted_by(request.COOKIES.get('sorted_by'))
    sort_for_paginator = sorted_by_number(request.COOKIES.get('sort'))
    state_sort_by_date = request.COOKIES.get('date', 0)

    if request.GET.get('date') or request.GET.get('price'):
        state_sort_by_date, order_by = sorted_by_date_or_price(request.GET)
    if request.GET.get('sort'):
        sort_for_paginator = sorted_by_number(request.GET.get('sort'))

    category_queryset = Category.objects.filter(level=0).annotate(num_adver=Count('advertisement'))
    category = get_object_or_404(category_queryset, slug=category_slug)
    advertisement_queryset = Advertisement.objects.filter(category=category.id, is_active=True,
                                                          moderation=True).select_related(
        'category', 'city').order_by(order_by)

    page_obj = variables_for_paginator(advertisement_queryset, request.GET.get('page'), sort_for_paginator)

    context = {
        "adver": advertisement_queryset,
        "category": category_queryset,
        "page_obj": page_obj,
        'date': state_sort_by_date,
    }

    response = render(request, 'param2.html', context)
    response.set_cookie('sort', sort_for_paginator)
    response.set_cookie('date', state_sort_by_date)
    response.set_cookie('sorted_by', order_by)

    return response


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
