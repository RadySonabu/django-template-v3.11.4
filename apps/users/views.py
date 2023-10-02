"""Views for user app."""
from django.shortcuts import render


# Create your views here.
def indexRate(request):
    """Index function."""
    return render(request, "base.html")
