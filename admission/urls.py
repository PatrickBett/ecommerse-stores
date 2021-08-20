from django.urls import path, include
from . import views
urlpatterns = [
    
    path('',views.admission , name='admission'),

    path('admission/contacts/',views.contacts , name='contacts'),       
]