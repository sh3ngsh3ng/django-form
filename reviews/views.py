from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm

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
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect("/review-success")
    else:
        form = ReviewForm()
        
    return render(request, "reviews/review.html", {
        # "has_error": True
        "form": form
    })


def review_success(request):
    return render(request, "reviews/success.html")