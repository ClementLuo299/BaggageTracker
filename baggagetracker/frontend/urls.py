from django.urls import path
from .views import index

#Add page urls
urlpatterns = [
    path('', index),
    path('login/', index),
    path('emplogin/',index),
    path('employees/<str:userID>', index),
    path('empcheckin', index)
    ]
