from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class PostPermission(models.Model):
    """
    This handles fine-grained access control per user per post
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='post_permissions'
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='permissions'
    )

    can_read = models.BooleanField(default=False)
    can_write = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'post')  # prevent duplicates

    def __str__(self):
        return f"{self.user} -> {self.post} (R:{self.can_read}, W:{self.can_write})"