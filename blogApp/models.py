from django.db import models
from django.utils import timezone
from userApp.models import UserProfile

class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    title = models.CharField(max_length=255, verbose_name="Title")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField("Title", max_length=300)
    featured_img = models.ImageField(null=True, blank=True)
    description = models.TextField()
    post_tag = models.ManyToManyField("Tag")
    category = models.ForeignKey(Category, verbose_name="Category")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False, verbose_name="Is published?")
    published_at = models.DateTimeField(null=True, blank=True, editable=False, verbose_name="Published at")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-created_at']

    def publish(self):
        self.is_published = True
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Tag(models.Model):
    tag_name = models.CharField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tag_name

class Comment(models.Model):
    comment_of = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

