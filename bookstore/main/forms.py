from django import forms

from bookstore.common.helpers import DisabledFieldsFormMixin
from bookstore.main.models import Book, Author, Event


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


class BookDeleteForm(DisabledFieldsFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._init_disabled_fields()
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Book
        fields = ('title', 'author', 'genre', 'description', 'cover_photo')


class AuthorCreateForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'description', 'picture', 'link')
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
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter author description',
                }
            ),
            'link': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Link to more details',
                }
            ),
        }


class AuthorEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'description', 'picture', 'link')


class AuthorDeleteForm(DisabledFieldsFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._init_disabled_fields()
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'description', 'picture', 'link')


class EventCreateForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('title', 'date', 'city', 'country', 'picture', 'link')
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter title',
                }
            ),
            'date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter date',
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter city location',
                }
            ),
            'country': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter country location',
                }
            ),
            'link': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Link to more details',
                }
            ),
        }


class EventEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Event
        fields = ('title', 'date', 'city', 'country', 'picture', 'link')


class EventDeleteForm(DisabledFieldsFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._init_disabled_fields()
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Event
        fields = ('title', 'date', 'city', 'country', 'picture', 'link')
 