from django.urls import path
from pages.views import Index

urlpatterns = [
    path('', Index.as_view(), name='index')
]