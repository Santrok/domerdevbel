
from django.urls import path

from .views import *

urlpatterns = [
    path('', get_main_page, name='home'),
    path('region_list/', RegionAPIView.as_view()),
    path('adver/', AdvertisementAPIView.as_view()),
    path('2/', get_main_page2),
    path('3/', get_main_page3),

]