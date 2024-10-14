# Imports
from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.book_search_view, name='general_search'),
]