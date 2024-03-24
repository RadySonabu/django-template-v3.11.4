"""Model for Profile."""

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(User):
    """Creates profile model."""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_profile"
    )
    # image = models.ImageField(
    # default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        """Return string of the object user."""
        return f"{self.user}"
