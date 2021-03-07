from django.urls import path
from .views import HomeView,Homeworks,HomeworkAdd
app_name='panels'
urlpatterns = [
    path('', HomeView.as_view(), name='HomePage'),
    path('Homeworks', Homeworks.as_view(), name='Homeworks'),
    path('Homeworks/Add', HomeworkAdd.as_view(), name='HomeworkAdd'),
    path('Homeworks/<int:id>', Homeworks.as_view()),
]