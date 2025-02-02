from django.urls import path
from .views import *
from  django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',index),
    path('create/',create),
    path('p/<uuid>/',post__),
    path('login/',login),
    path('signup/',signup),
    path('test/',test)
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
