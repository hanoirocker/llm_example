from django.urls import path
from .views import GenerateTextView

# Define the URL patterns for the API

urlpatterns = [
    path("chat/", GenerateTextView.as_view(), name="generate_text"),
]