from django.urls import path
from orgApp import views

app_name = "orgApplication"

urlpatterns = [
    path("", views.self_org, name='self_org'),
]
