from django.urls import path
from sellerapp.views import home, index, form, create, view, edit, update,\
    delete, index_address, create_address, edit_address, delete_address,\
    update_address, form_address, view_address


urlpatterns = [
    path('', home, name='home'),
    path('index/', index, name='index'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),

    # Address

    path('index_address/', index_address, name='index_address'),
    path('form_address/', form_address, name='form_address'),
    path('create_address/', create_address, name='create_address'),
    path('view_address/<int:pk>/', view_address, name='view_address'),
    path('edit_address/<int:pk>/', edit_address, name='edit_address'),
    path('update_address/<int:pk>/', update_address, name='update_address'),
    path('delete_address/<int:pk>/', delete_address, name='delete_address'),

]
