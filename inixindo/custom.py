from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.db.models import Q


class CustomAuth(ModelBackend):
    def authenticate(self, request, account_id=None, password=None):
        try:
            user = User.objects.get(Q(email=account_id) | Q(username=account_id))
            valid = check_password(password, user.password)
            if valid:
                return user
            else:
                return None
        except User.DoesNotExist:
            # Create a new user. There's no need to set a password
            # because only the password from settings.py is checked.
            return None


    # def get_user(self, user_id):
    #     try:
    #         return User.objects.get(pk=user_id)
    #     except User.DoesNotExist:
    #         return None