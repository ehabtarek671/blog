from django.db import models
from func import saveimage
class Account(models.Model):
    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=500, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    profile_image = models.ImageField(upload_to=saveimage.user_profile_image_path, null=True, blank=True)

    def __str__(self):
        return self.name
