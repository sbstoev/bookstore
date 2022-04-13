from django import forms

from bookstore.main.models import Book


class CreateBookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'author', 'genre', 'description', 'cover_photo')
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter book tile',
                }
            ),
            'author': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter book author',
                }
            ),
            # 'genre': forms.SelectMultiple(
            #     attrs={
            #         'class': 'form-control',
            #         'placeholder': 'Choose genre',
            #     }
            # ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter book description',
                }
            ),

        }


class BookEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Book
        fields = ('title', 'author', 'genre', 'description', 'cover_photo')
        # exclude = ('user_profile',)


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