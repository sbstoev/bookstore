from django.urls import path

import bookstore.main.views
from bookstore.main.views import HomeView, DashboardView, AboutUsView, CreateBookView, BookDetailsView, BookEditView, \
    BookDeleteView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),     # <- landing page
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('about_us/', AboutUsView.as_view(), name='about us'),

    path('book/details/<int:pk>/', BookDetailsView.as_view(), name='book details'),
    path('book/add/', CreateBookView.as_view(), name='create book'),
    path('book/edit/<int:pk>/', BookEditView.as_view(), name='edit book'),
    path('book/delete/<int:pk>/', BookDeleteView.as_view(), name='delete book'),

    # path('404/', page_not_found, name='page not found'),
)


