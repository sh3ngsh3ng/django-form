from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your name", max_length=50, error_messages={
#         "required": "Your name must not be empty",
#         "max_length": "Please enter a shorter name!"
#     })
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)


# Using model as form
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        # fields = ["user_name", "review_text", "rating"] # selecting fields to show in form
        # exclude = ['owner_comments'] # setting fields to exclude. can use the above as well
        labels = {
            'user_name': "Your name",
            "review_text": "Your Feedback",
            "rating": "Your Rating"
        }

        error_messages = {
            "user_name": {
                "required": "Your name must not be empty!",
                "max_length": "Please entter a shorter name!"
            }
        }
