from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import *

# Register your models here.

class PhotoInlines(admin.StackedInline):
  model = Photo
  max_num = 10
  extra = 0
class RegionAdmin(MPTTModelAdmin):
    prepopulated_fields = {"slug": ("region",)}

class CategoryAdmin(MPTTModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class AdvertisementAdmin(admin.ModelAdmin):
    inlines = [PhotoInlines,]
    prepopulated_fields = {"slug": ("title",)}

class PhotoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class GalleryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}



admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Advertisement, AdvertisementAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Photo, PhotoAdmin)

