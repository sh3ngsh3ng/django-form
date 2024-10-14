from django.urls import path

from . import views

urlpatterns = [
    path("", views.review),
    path("review-success", views.review_success)
]