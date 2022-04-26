import django
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookstore.main.urls')),
    path('accounts/', include('bookstore.accounts.urls')),
    # path('404/', custom_page_not_found),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'bookstore.views.page_not_found_view'

