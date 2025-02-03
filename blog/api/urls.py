from django.urls import path
from .views import *

urlpatterns = [
    path('blogs/',send_posts),
    path('me/',send_user),
    path('like/',NewLike),
    path('dislike/',NewDisLike),
    path('checklike/<uuid>',checklike)
]
