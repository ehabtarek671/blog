from django.urls import path
from .views import *

urlpatterns = [
    path('blogs/',send_posts),
    path('user/',send_user)
]
