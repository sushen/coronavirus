from django.contrib import admin
from orgApp import models

# Register your models here.

admin.site.register(models.Organisation)
admin.site.register(models.Category)
admin.site.register(models.orgDetail)
admin.site.register(models.orgProject)
