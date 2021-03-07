from django.urls import path
from .views import HomeView
app_name='panels'
urlpatterns = [
    path('', HomeView.as_view(), name='HomePage'),
]