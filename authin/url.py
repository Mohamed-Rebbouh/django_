from django.urls import path
from.views import SignIn,Login_user,sscc

urlpatterns = [
    
    path('singin/',SignIn, name='signin'),
    path('login/',Login_user,name='login'),
    path('succsec/',sscc,name='succsec')
]