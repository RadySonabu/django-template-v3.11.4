"""User Forms."""
from allauth.account.forms import LoginForm


class MyCustomLoginForm(LoginForm):
    """Custom login form."""

    def login(self, *args, **kwargs):
        """Implement login method."""
        # Add your own processing here.
        print("this is login")
        # You must return the original result.
        return super(MyCustomLoginForm, self).login(*args, **kwargs)
