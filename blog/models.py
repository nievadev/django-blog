from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length = 100)

    # CharField similar to TextField, CharField is for short strings and TextField for larger
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # This method is for making the Post.object.all() query set more descriptive.
    def __str__(self):
        return self.title

    # Arguments:
    # auto_now = True (means that we would update date_posted to the current date time everytime the post gets updated)
    # auto_now_add = True (means that date_posted can't change and will only have the date time what the Post object was created)
    # default = timezone.now (requires from django.utils import timezone)
    # on_delete=models.CASCADE (means that once the author is deleted, Post objects get deleted as well)

    # Why default argument? see in video
