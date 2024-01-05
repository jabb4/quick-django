from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import User


class AuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        if username and password:
            try:
                user = User.objects.get(username=username)
                if check_password(password, user.password):
                    if user.is_active:
                        return user
            except User.DoesNotExist:
                return None
        return None

    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None
