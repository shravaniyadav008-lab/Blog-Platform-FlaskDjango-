from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):

    CATEGORY_CHOICES = [
        ('Technology', 'Technology'),
        ('Programming', 'Programming'),
        ('Education', 'Education'),
        ('Lifestyle', 'Lifestyle'),
        ('Travel', 'Travel'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=200)

    content = models.TextField()

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blogs'
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='Other'
    )

    image = models.URLField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Comment(models.Model):

    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    text = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.author.username} - {self.blog.title}"