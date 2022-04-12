from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from bookstore.accounts.views import UserRegisterView, UserLoginView, UserLogoutView, ProfileDetailsView, \
    ProfileEditView, ChangeUserPasswordView, FavouritesDetailsView, FavouritesDeleteView, \
    favourite_add

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='register'),                     # <- 1 page, 1 form
    path('login/', UserLoginView.as_view(), name='login_user'),                         # <- 1 page, 1 form
    path('logout/', UserLogoutView.as_view(), name='logout user'),
    path('<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),            # <- 1 page
    path('edit/<int:pk>/', ProfileEditView.as_view(), name='profile edit'),                      # <- 1 page, 1 form
    # path('delete/', ProfileDeleteView.as_view(), name='profile delete'),                  # <- 1 page
    path('edit_password/', ChangeUserPasswordView.as_view(), name='change password'),   # <- 1 page, 1 form
    path('change_password_done/', RedirectView.as_view(url=reverse_lazy('dashboard')), name='change_password_done'),
    path('favourites/<int:pk>/', FavouritesDetailsView.as_view(), name='favourites details'),
    path('favourites/add/<int:pk>/', favourite_add, name='favourite add'),
    path('favourites/delete/<int:pk>/', FavouritesDeleteView.as_view(), name='favourites delete'),
)
