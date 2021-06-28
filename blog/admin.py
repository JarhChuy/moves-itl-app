from django.contrib import admin
from .models import Post, Comment

class CommentInLine(admin.TabularInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)