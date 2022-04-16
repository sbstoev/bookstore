from django import forms
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth import forms as auth_forms

from bookstore.accounts.models import Profile
from bookstore.common.helpers import BootstrapFormMixin
from bookstore.main.models import Book


class CreateProfileForm(auth_forms.UserCreationForm):

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

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
            auth_user = authenticate(
                username=self.cleaned_data['username'],
                password=self.cleaned_data['password1']
            )
            login(self.request, auth_user)
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


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()
