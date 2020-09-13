from .models import Post
from newsboard.celery import app


@app.task
def reset_upvote_amount():
    Post.objects.all().update(upvotes_amount=0)
