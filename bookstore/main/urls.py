from django.urls import path

from bookstore.main.views import HomeView, DashboardView, AboutUsView, CreateBookView, BookDetailsView, BookEditView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),     # <- landing page
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('about_us/', AboutUsView.as_view(), name='about us'),

    path('book/details/<int:pk>/', BookDetailsView.as_view(), name='book details'),
    path('book/add/', CreateBookView.as_view(), name='create book'),
    path('book/edit/<int:pk>/', BookEditView.as_view(), name='edit book'),
    # path('book/delete/<int:pk>/', DeleteBookView.as_view(), name='delete book'),

    # path('photo/add/', CreateBookPhotoView.as_view(), name='create book photo'),
    # path('photo/like/<int:pk>/', like_book_photo, name='like book photo'),
    # path('photo/edit/<int:pk>/', EditBookPhotoView.as_view(), name='edit book photo'),
)
