
from django.urls import path
from . import views

urlpatterns = [
    path('aboutus/',views.aboutus,name='aboutus'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/register/', views.register, name='register'),

    path('databaselist/', views.DetailsView.as_view(), name='databaselist'),

    path('logout/', views.logout, name='logout'),
    path('login/passwordreset/', views.password_reset, name='passwordreset'),

    path('aboutus/ict/',views.ict,name='ict'),
    path('aboutus/plumbing/',views.plumbing,name='plumbing'),
    path('aboutus/Electrical/',views.Electrical,name='Electrical'),
    path('aboutus/hair_beauty/',views.hair_beauty,name='hair_beauty'),

    path('login/account/', views.account, name='account'),
   # path('sendmail/', views.sendmail, name='sendmail'),
]
