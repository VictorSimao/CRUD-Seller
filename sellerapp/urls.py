from django.urls import path
from sellerapp.views import home, index, form, create, view, edit, update,\
    delete


urlpatterns = [
    path('', home, name='home'),
    path('index', index, name='index'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),

]
