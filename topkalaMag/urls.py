
from django.urls import path
from . import views

app_name = 'topkalaMag'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('categories/', views.CategoriesView.as_view(), name='categories'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('search-results/', views.SearchResultsView.as_view(), name='search-results'),
    path('single-post/<int:pk>/', views.SinglePostView.as_view(), name='single-post'),
    path('error404/', views.Error404View.as_view(), name='error404'),


]