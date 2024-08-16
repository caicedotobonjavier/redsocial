from django.contrib import admin
#
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'content',
        'image',
        'user',
    )

admin.site.register(Post, PostAdmin)