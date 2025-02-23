from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list =['title', 'author', 'created_at', 'id']
    fields = ['title', 'content']

class CommentAdmin(admin.ModelAdmin):
    list = ['content', 'author', 'created_at']
    fields = ['content']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)