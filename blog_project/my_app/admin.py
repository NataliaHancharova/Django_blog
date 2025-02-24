from django.contrib import admin
from .models import Post, Comment

@admin.action(description='Delete content')
def del_content(modeladmin, request, queryset):
    queryset.update(content = '')


@admin.action(description='make a headline upperset')
def upper_title(modeladmin, request, queryset):
    for post in queryset:
        post.title = post.upper_title()
        post.save()


# @admin.actions(description='make a headline lowerset')
# def lower_title(modeladmin, request, queryset):
#     for post in queryset:
#         post.title = post.lower.title()
#         post.save()


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class PostAdmin(admin.ModelAdmin):
    list_display =('title', 
                   'author',
                   'created_at',
                   'content',
                   )
    
    list_filter = ('author',
                   'created_at',

                  )

    search_fields = ['title',
                    'content',
                    ]
    
    ordering = ('-created_at',)
    inlines = [CommentInline]
    actions = [del_content, upper_title]


class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'created_at')
    search_fields = ['content']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
