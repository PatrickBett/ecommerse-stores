from django.urls import path
from .views import ShopView , EmailSuccessView ,SearchResultView, PurchasesView
from . import views

urlpatterns = [

    path('',ShopView.as_view(),name='shop'),

    path('search/',SearchResultView.as_view(),name='searchresult'),

    path('emailsuccess/',EmailSuccessView.as_view(),name='emailsuccess'),
    path('emailmessage/',views.mail,name='emailmessage'),
#Specifies url for purchases made
    path('purchases/',PurchasesView.as_view(),name='purchases'),
    
 
]