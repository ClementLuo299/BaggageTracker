from django.urls import path

#Import views
from .views import UsrView

urlpatterns = [
    path('usr', UsrView.as_view())
]