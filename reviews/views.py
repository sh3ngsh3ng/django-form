from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class ReviewView(View):
    def get():
        pass

    def post():
        pass

# Create your views here.
def review(request):
    # if request.method == 'POST':
    #     entered_username = request.POST['username']
    #     if entered_username == "":
    #         return render(request, "reviews/review.html", {
    #             "has_error": True
    #         })
    #     return HttpResponseRedirect("/review-success")

    if request.method == "POST":
        # Updating with models form
        # existing_model = Review.objects.get(pk=1)
        # form = ReviewForm(request.POST, instance=existing_model)

        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # Saving with model
            # review = Review(user_name=form.cleaned_data['user_name'], 
            #                 review_text=form.cleaned_data['review_text'], 
            #                 rating=form.cleaned_data['rating'])
            # review.save()

            # Saving with model form
            form.save()

            return HttpResponseRedirect("/review-success")
    else:
        form = ReviewForm()
        
    return render(request, "reviews/review.html", {
        # "has_error": True
        "form": form
    })


# def review_success(request):
#     return render(request, "reviews/success.html")

class ThankYouView(TemplateView):
    template_name = "review/success.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['message'] = "Hear from you soon!"
        return context
    

class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    # exposed in template as object_list by default
    # use for loop on object_list
    # if not, configure the object_list name as below
    context_object_name = "review"
    # now can use review in template instead of object_list

    # for modifying query, no need if returning the whole list
    def get_queryset(self) -> QuerySet[Any]:
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=4)
        return data


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
    