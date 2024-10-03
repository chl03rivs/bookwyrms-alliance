from django.urls import path, include

urlpatterns = [
    path('accounts/', include('allauth.urls')),  # Includes all the Allauth views
]
