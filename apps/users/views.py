"""Views for user app."""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def indexRate(request):
    """Index function."""
    return render(request, "base.html")


def public_home(request):
    """Public view."""
    return render(request, "public_home.html")


@login_required
def private_home(request):
    """Private view."""
    return render(request, "private_home.html")
