from django.db import models
from userApp.models import UserProfile



class Category(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    title = models.CharField(max_length=255, verbose_name="Title")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return self.title

class Organisation(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    about = models.TextField()
    org_category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE)
    division = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    thana = models.CharField(max_length=255)
    postal_area = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.EmailField(max_length=255, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    objects = models.QuerySet()

    def __str__(self):
        return self.owner

class orgDetail(models.Model):
    org_id = models.OneToOneField(Organisation, on_delete=models.CASCADE)
    image = models.ImageField()
    logo = models.ImageField()
    description = models.TextField()
    facebook_url = models.URLField()
    twitter_url = models.URLField()
    youtube_url = models.URLField()
    website_url = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.org_id

class orgProject(models.Model):
    name = models.CharField(max_length=255)
    area = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    details = models.TextField()
    duration = models.DateTimeField()
    image = models.ImageField()
    budget = models.CharField(max_length=255)
    status = models.TextField(verbose_name="Status")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name




