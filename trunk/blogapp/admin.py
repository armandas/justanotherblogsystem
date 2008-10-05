from django.contrib import admin

from blogapp.models import Tag
from blogapp.models import Post, Page
from blogapp.models import Comment
from blogapp.models import Option

class TagAdmin(admin.ModelAdmin):
    list_per_page = 15

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date',)
    list_filter = ('disable_comments', 'tags',)
    ordering = ('-date',)
    search_fields = ('title', 'content')
    list_per_page = 15

    #experimental
    filter_horizontal = ('tags',)

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date',)
    ordering = ('name',)
    search_fields = ('title', 'content')
    list_per_page = 15

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'content', 'post', 'date', 'comment_type')
    list_filter = ('comment_type', 'post')
    ordering = ('-date',)
    search_fields = ('author_name', 'author_email', 'author_website', 'author_ip', 'content')
    list_per_page = 15

class OptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
    ordering = ('name',)
    search_fields = ('name', 'value')
    list_per_page = 15

admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Option, OptionAdmin)
