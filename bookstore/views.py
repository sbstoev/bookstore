from django.shortcuts import render
from django.views import generic as views


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
