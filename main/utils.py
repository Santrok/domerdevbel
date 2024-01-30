from django.core.paginator import Paginator


def sorted_by_number(number):
    if (number == '3'
            or number == '6'
            or number == '9'):
        sort_for_paginator = int(number)
        return sort_for_paginator


def variables_for_paginator(queryset=None, elments=None, page=None):
    paginator = Paginator(queryset, elments)
    page_number = page
    page_obj = paginator.get_page(page_number)
    return page_obj
