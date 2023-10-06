
from django.urls import path
from . import views

app_name = 'topkalaAdmin'

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('index2/', views.Index2View.as_view(), name='index2'),
    path('starter/', views.StarterView.as_view(), name='starter'),
]
