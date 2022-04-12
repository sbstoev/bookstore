from django.contrib.auth import views as auth_views, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import mixins as auth_mixins
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from bookstore.accounts.form import CreateProfileForm, EditProfileForm
from bookstore.accounts.models import Profile
from bookstore.common.view_mixins import RedirectToDashboard
from bookstore.main.models import Book


class UserRegisterView(RedirectToDashboard, views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('dashboard')


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url() # <-- gets the default success_url (accounts/profile)


class UserLogoutView(auth_views.LogoutView):
    pass


class ProfileDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'


class ProfileEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Profile
    template_name = 'accounts/profile_edit.html'
    fields = (
        'first_name',
        'last_name',
        'picture',
        'date_of_birth',
        'description',
        'email',
        'gender',
    )

    def get_success_url(self):  # <-- because we need to give a pk
        return reverse_lazy('profile details', kwargs={'pk': self.object.user_id})


class ChangeUserPasswordView(auth_mixins.LoginRequiredMixin, auth_views.PasswordChangeView):
    template_name = 'accounts/change_password.html'


# class ProfileDeleteView(views.DeleteView):
#     template_name = 'accounts/profile_delete.html'
#     form_class = DeletePetForm

# class FavouritesAddView(views.CreateView):
#     pass

@login_required
def favourite_add(request, pk):
    books = Book.objects.all()
    book = Book.objects.get(pk=pk)
    if book.favourites.filter(pk=request.user.pk).exists():
        book.favourites.remove(request.user)
    else:
        book.favourites.add(request.user)

    context = {
        'books': books
    }
    return render(request, 'main/dashboard.html', context)


class FavouritesDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = get_user_model()
    template_name = 'accounts/favourites_details.html'
    context_object_name = 'user'
    books = Book.objects.all()

    def get_queryset(self):  # <- replace prefetch_related
        queryset = super().get_queryset()

        queryset.prefetch_related('favourites')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # This checks if the current user in the owner:
        context['favourites'] = self.books.filter(favourites=self.request.user)

        return context


class FavouritesDeleteView(views.DeleteView):
    pass
