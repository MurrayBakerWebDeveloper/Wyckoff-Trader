from django.shortcuts import render_to_response

from .models import BlogArticle


def page_with_links(request):
    return render_to_response(
        'blog_list.html',
        context={
            'blogs': BlogArticle.objects.all(),
        }
    )