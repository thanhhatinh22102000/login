from .views import IndexClass,LoginClass,View
from django.urls import path

urlpatterns = [
    path('',IndexClass.as_view(),name='indexclass'),
    path('login/',LoginClass.as_view(),name='loginclass'),
    path('viewinfo/',View,name='viewinfo'),
]