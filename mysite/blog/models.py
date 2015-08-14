from django.db import models
from django.contrib.auth.models import User


class BlogArticle(models.Model):
    author = models.ForeignKey(User, null=False, blank=False)
    title = models.CharField(max_length=63, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    publish_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class BlogComment(models.Model):
    author = models.ForeignKey(User, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return 'Comment from {} on {}'.format(self.author, self.comment_date)