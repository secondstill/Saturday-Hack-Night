from django.urls import path
from .views import yourl, urlRedirect

urlpatterns = [
    path('', yourl, name='yourl'),
    path('<slug:slug>/', urlRedirect, name='urlRedirect'),
]
