from django.urls import path
from .views import EmailListView

urlpatterns = [
    path('email/', EmailListView.as_view(), name='email'),
]