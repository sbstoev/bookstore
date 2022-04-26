from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from bookstore.accounts.models import Profile
from bookstore.common.view_mixins import RedirectToDashboard
from bookstore.main.forms import CreateBookForm, BookEditForm, BookDeleteForm

from bookstore.main.models import Book


class HomeView(views.TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context


class DashboardView(views.ListView):
    model = Book
    template_name = 'main/dashboard.html'
    context_object_name = 'books'  # rename the object from class Book


class AboutUsView(views.ListView):
    model = Book
    template_name = 'main/about_us.html'
    # context_object_name = 'books'  # rename the object from class Book


class CreateBookView(views.CreateView):
    template_name = 'main/book_create.html'
    form_class = CreateBookForm

    success_url = reverse_lazy('dashboard')

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs['user'] = self.request.user
    #     return kwargs


class BookDetailsView(views.DetailView):
    model = Book
    template_name = 'main/book_details.html'
    context_object_name = 'book'


class BookEditView(views.UpdateView):
    model = Book
    template_name = 'main/book_edit.html'
    form_class = BookEditForm

    success_url = reverse_lazy('dashboard')


class BookDeleteView(views.DeleteView):
    model = Book
    template_name = 'main/book_delete.html'
    form_class = BookDeleteForm

    success_url = reverse_lazy('dashboard')
