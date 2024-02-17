from django.urls import path
from .views import add_member,affich,remove_member,edit_member

urlpatterns = [
    
    path('add/',add_member, name='add_member'),
    path('affiche/',affich,name='affich_member'),
    path('remove/<int:member_id>/', remove_member, name='remove_member'),
    path('edit/<int:member_id>/', edit_member, name='edit_member')
]