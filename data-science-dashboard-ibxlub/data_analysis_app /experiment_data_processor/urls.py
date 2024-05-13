from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_csv, name='upload_csv'),
    path('data/', views.display_data, name='display_data'),
    path('get_data/', views.get_data, name='get_data'),  # Add URL mapping for get_data view
]


