from django.urls import path
from .views import *

urlpatterns = [
    path('blogs/',send_posts),
    path('me/',send_user)
]
