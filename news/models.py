from django.db import models
from django.db.models import F


class Post(models.Model):
    title = models.CharField(max_length=300)
    creation_date = models.DateTimeField(auto_now_add=True)
    upvotes_amount = models.PositiveIntegerField(default=0)
    author_name = models.CharField(max_length=40)

    def __str__(self):
        return self.title

    def upvote(self):
        self.upvotes_amount = F("upvotes_amount") + 1
        self.save()
        self.refresh_from_db()


class Comment(models.Model):
    author_name = models.CharField(max_length=40)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
