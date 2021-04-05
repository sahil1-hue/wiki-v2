from django.urls import path
from .views import*
urlpatterns = [
    path('', wikiSearch,name="wikiHome"),
]