"""Views for user app."""
from django.shortcuts import render


# Create your views here.
def index(request):
    """Index function."""
    return render(request, "base.html")
