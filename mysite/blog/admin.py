from django.contrib import admin

from .models import BlogArticle, BlogComment



class BlogArticleAdmin(admin.ModelAdmin):
    pass
admin.site.register(BlogArticle, BlogArticleAdmin)


class BlogCommentAdmin(admin.ModelAdmin):
    pass
admin.site.register(BlogComment, BlogCommentAdmin)