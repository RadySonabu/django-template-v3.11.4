"""Views for user app."""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def indexRate(request):
    """Index function."""
    number_of_cards = 1234567

    return render(
        request,
        "base.html",
        context={"number_of_cards": number_of_cards, "name": "random name"},
    )


def public_home(request):
    """Public view."""
    return render(request, "public_home.html")


@login_required
def private_home(request):
    """Private view."""
    number_of_cards = 12
    return render(
        request,
        "private_home.html",
        context={"number_of_cards": number_of_cards, "name": "random name"},
    )


@login_required
def create_profile(request):
    """Private view."""
    number_of_cards = 12
    return render(
        request,
        "private_home.html",
        context={"number_of_cards": number_of_cards, "name": "random name"},
    )
