from django.urls import path

import bookstore.main.views
from bookstore.main.views import HomeView, DashboardView, AboutUsView, CreateBookView, BookDetailsView, BookEditView, \
    BookDeleteView, AuthorsView, AuthorCreateView, AuthorEditView, \
    AuthorDeleteView, EventCreateView, EventEditView, EventDeleteView, EventsView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),     # <- landing page
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('about_us/', AboutUsView.as_view(), name='about us'),
    path('authors/', AuthorsView.as_view(), name='authors'),
    path('events/', EventsView.as_view(), name='events'),

    path('book/details/<int:pk>/', BookDetailsView.as_view(), name='book details'),
    path('book/add/', CreateBookView.as_view(), name='create book'),
    path('book/edit/<int:pk>/', BookEditView.as_view(), name='edit book'),
    path('book/delete/<int:pk>/', BookDeleteView.as_view(), name='delete book'),

    path('author/add', AuthorCreateView.as_view(), name='author create'),
    path('author/edit/<int:pk>/', AuthorEditView.as_view(), name='author edit'),
    path('author/delete/<int:pk>/', AuthorDeleteView.as_view(), name='author delete'),

    path('event/add', EventCreateView.as_view(), name='event create'),
    path('event/edit/<int:pk>/', EventEditView.as_view(), name='event edit'),
    path('event/delete/<int:pk>/', EventDeleteView.as_view(), name='event delete'),

    # path('404/', page_not_found, name='page not found'),
)


