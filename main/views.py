from datetime import datetime, date, timedelta

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .forms import PhotoForm
from .models import Advertisement, Region, Category
from .serializers import (RegionSerializer,
                          CategorySerializer,
                          AdvertisementSerializer)


# Create your views here.

def get_main_page(request):
    advertisement_queryset = Advertisement.objects.filter(is_active=True,
                                                          moderation=True).order_by("-date_of_create")

    context = {
        "adver": advertisement_queryset,

    }
    return render(request, 'param1.html', context)

def get_main_page2(request):
    advertisement_queryset = Advertisement.objects.filter(is_active=True,
                                                          moderation=True).order_by("-date_of_create")

    context = {
        "adver": advertisement_queryset,

    }
    return render(request, 'param2.html', context)

def get_main_page3(request):
    advertisement_queryset = Advertisement.objects.filter(is_active=True,
                                                          moderation=True).order_by("-date_of_create")

    context = {
        "adver": advertisement_queryset,

    }
    return render(request, 'param3.html', context)

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
