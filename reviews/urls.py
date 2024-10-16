from django.urls import path

from . import views

urlpatterns = [
    path("", views.review),
    # path("class", views.ReviewView.as_view())
    # path("review-success", views.review_success)
    path("review-success", views.TemplateView.as_view()),
    path("reviews/<int:pk>", views.SingleReviewView.as_view())
]