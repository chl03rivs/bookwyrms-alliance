"""
URL configuration for bookwyrms_alliance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Imports
from django.contrib import admin
from django.urls import path, include

from data import views as data_views
from books.services.google_books import book_search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
    path('users/', include('users.urls')),
    path('books/', include('books.urls')),
    path('', data_views.home_view, name='home'),
    path('help/', data_views.help_view, name='help'),
    path('community/', include('data.urls')),
]
