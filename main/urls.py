
from django.urls import path

from .views import *

urlpatterns = [
    path('', get_main_page, name='param1'),
    path('fetch/', fetch_zapros, name='fetch'),
    path('region_list/', RegionAPIView.as_view()),
    path('adver/', AdvertisementAPIView.as_view()),
    path('2/', get_main_page2, name='param2'),
    path('3/', get_main_page3),
    path('advertisement/<slug:category_slug>/', get_advertisement_by_category, name='adver_by_category'),
    path('advertisement2/<slug:category_slug>/', get_advertisement_by_category2, name='adver_by_category2')

]