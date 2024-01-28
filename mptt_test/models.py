from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


# Create your models here.
class Category(MPTTModel):
    CATEGORY_4 = 'category_4'
    CATEGORY_3 = 'category_3'
    CATEGORY_2 = 'category_2'
    CATEGORY_1 = 'category_1'

    type_choices = [
        (CATEGORY_4, ("category_4")),
        (CATEGORY_3, ("category_3")),
        (CATEGORY_2, ("category_2")),
        (CATEGORY_1, ("category_1")),
    ]
    name = models.CharField(max_length=100)
    type = models.CharField(choices=type_choices, max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name