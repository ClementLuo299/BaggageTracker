from django.urls import path
from .views import UsrView

urlpatterns = [
    path('', UsrView.as_view())
]