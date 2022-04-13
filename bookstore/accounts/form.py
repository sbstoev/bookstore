from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms

from bookstore.accounts.models import Profile
from bookstore.common.helpers import BootstrapFormMixin


class CreateProfileForm(auth_forms.UserCreationForm):

    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter first name',
        }
        )
    )

    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter last name',
        }
        )
    )

    picture = forms.ImageField()

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'name@gmail.com',
        }
        )
    )

    address = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '1234 Main St',
        }
        )
    )

    city = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter City',
        }
        )
    )

    zip = forms.CharField(
        max_length=5,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Zip',
        }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            picture=self.cleaned_data['picture'],
            email=self.cleaned_data['email'],
            address=self.cleaned_data['address'],
            city=self.cleaned_data['city'],
            zip=self.cleaned_data['zip'],
            user=user)

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter user name',
                }
            ),
            'password1': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter password',
                }
            ),
            'password2': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter password',
                }
            ),
        }


class EditProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'picture', 'email', 'address', 'city', 'zip')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter last name',
                }
            ),
            # 'picture': forms.TextInput(
            #     attrs={
            #         'class': 'form-control',
            #         'placeholder': 'Enter URL',
            #     }
            # ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'name@gmail.com',
                }
            ),
            'address': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': '1234 Main St',
                }
            ),
            'city': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter City',
                }
            ),
            'zip': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Zip',
                }
            ),
        }


# class DeleteProfileForm(forms.ModelForm):
#     def save(self, commit=True):
#         pets = list(self.instance.pet_set.all())
#         # should be done with signals
#         # because this breaks the abstraction of the auth app
#         PetPhoto.objects.filter(tagged_pet__in=pets).delete()
#         self.instance.delete()
#
#         return self.instance
#
#     class Meta:
#         model = Pet
#         fields = ()
