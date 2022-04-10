from django import forms

from bookstore.common.helpers import BootstrapFormMixin
from bookstore.main.models import Book


class CreateBookForm(forms.ModelForm):
    # def __init__(self, user, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.user = user
    #     # self._init_bootstrap_form_controls()
    #
    # def save(self, commit=True):
    #     book = super().save(commit=False)   # <-- get book instance, with commit=False, so it doesn't go to the base
    #     book.user = self.user
    #     if commit:
    #         book.save()

    class Meta:
        model = Book
        fields = ('title', 'author', 'genre', 'description', 'cover_photo')
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Enter book tile',
                }
            ),
            'author': forms.TextInput(
                attrs={
                    'placeholder': 'Enter book author',
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Enter book description',
                }
            ),
        }


# class EditPetForm(BootstrapFormMixin, forms.ModelForm):
#     MIN_DATE_OF_BIRTH = date(1920, 1, 1)
#     MAX_DATE_OF_BIRTH = date.today()
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self._init_bootstrap_form_controls()
#
#     # def clean_date_of_birth(self):
#     #     MaxDateValidator(date.today())(self.cleaned_data['date_of_birth'])
#     #     return self.cleaned_data['date_of_birth']
#
#     class Meta:
#         model = Pet
#         exclude = ('user_profile',)
#
#
# class DeletePetForm(BootstrapFormMixin, DisabledFieldsFormMixin, forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self._init_bootstrap_form_controls()
#         self._init_disabled_fields()
#
#     def save(self, commit=True):
#         self.instance.delete()
#         return self.instance
#
#     class Meta:
#         model = Pet
#         exclude = ('user_profile',)