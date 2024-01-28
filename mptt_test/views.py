from django.shortcuts import render

from .forms import CategoryForm, StoreForm
from .models import Category


# Create your views here.
def get_form(request):
    category = Category.objects.all()
    form = StoreForm

    context = {
        'form': form,
        'category': category
    }
    return render(request, 'mptt.html', context)