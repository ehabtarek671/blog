from django.contrib import admin
from .models import Post,Comment,Account,Like,DisLike
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Account)
admin.site.register(Like)
admin.site.register(DisLike)