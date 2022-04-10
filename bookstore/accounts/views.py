from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import mixins as auth_mixins
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from bookstore.accounts.form import CreateProfileForm, EditProfileForm
from bookstore.accounts.models import Profile
from bookstore.common.view_mixins import RedirectToDashboard


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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # self.object is a Profile
    #     pets = list(Pet.objects.filter(user_id=self.object.user_id))
    #
    #     pet_photos = PetPhoto.objects.filter(tagged_pets__in=pets).distinct()
    #
    #     total_likes_count = sum(pp.likes for pp in pet_photos)
    #     total_pet_photo_count = len(pet_photos)
    #
    #     context.update({
    #         'total_likes_count': total_likes_count,
    #         'total_pet_photos_count': total_pet_photo_count,
    #         'is_owner': self.object.user == self.request.user,
    #         'pets': pets,
    #     })
    #
    #     return context


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


# class DeletePetView(views.DeleteView):
#     template_name = 'accounts/profile_delete.html'
#     form_class = DeletePetForm
