from django.urls import path
from .views import *

urlpatterns = [
    path('blogs/',send_posts),
    path('me/',send_user),
    path('like/<uuid>',NewLike),
    path('dislike/<uuid>',NewDisLike),
    path('checklike/<uuid>',checklike)
]
