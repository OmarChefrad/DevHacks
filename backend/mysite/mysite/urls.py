from django.urls import path
from myapp.views import get_data

urlpatterns = [
    path('api/data/', get_data, name='get_data'),
]
