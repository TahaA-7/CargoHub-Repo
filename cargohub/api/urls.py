from django.urls import path
from . import views  # Import views from the same directory

urlpatterns = [
    path('clients/', views.client_list, name='client_list'), 
]