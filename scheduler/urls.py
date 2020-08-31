from django.contrib import admin
from django.urls import path
from .import views
from .views import Scheduler

urlpatterns = [
    path('', Scheduler.as_view()),
]