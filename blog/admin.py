from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Comment, Post, Link

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "body", "post", "created_on", "active")
    list_filter = ("active", "created_on")
    search_fields = ("name", "email", "body")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

class LinkAdmin(SummernoteModelAdmin):
    list_display = ("title",)
    summernote_fields = ("content",)

class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", "slug", "status", "lang", "created_on")
    list_filter = ("status", "lang", "created_on")
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)

admin.site.register(Post, PostAdmin)
admin.site.register(Link, LinkAdmin)
