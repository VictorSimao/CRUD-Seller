from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('form/', views.form),
    path('save/', views.save),
    path('delete/', views.delete),
    path('configs/', views.index),
    path('configs/form/', views.form),
    path('configs/form/save/', views.save),
    path('configs/delete/', views.delete),
]
