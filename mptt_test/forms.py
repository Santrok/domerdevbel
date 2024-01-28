from django import forms
from mptt.forms import TreeNodeChoiceField, TreeNodeMultipleChoiceField

from .models import Category


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = "__all__"


class StoreForm(forms.Form):
    category = TreeNodeMultipleChoiceField(queryset=Category.objects.all(), level_indicator='+')