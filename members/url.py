from django.urls import path
from .views import add_member,affich

urlpatterns = [
    
    path('add/',add_member, name='add_member'),
    path('affiche/',affich,name='affich_member')

]