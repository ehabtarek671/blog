from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('create/',create),
    path('p/<uuid>/',post__)
]
