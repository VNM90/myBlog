from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + self.author

    def get_absolute_url(self):
        return reverse_lazy('home')


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    # body = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.post.title + ' | ' + self.author

    def get_absolute_url(self):
        return reverse_lazy('home')
