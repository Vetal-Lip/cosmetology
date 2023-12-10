from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('record/', views.record, name='record'),
    path('category/<int:category_id>/', views.show_category, name='category'),
]
