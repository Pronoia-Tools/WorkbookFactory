from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404
from users.models import Subscription


class Ownership(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class Subscriber(UserPassesTestMixin):
    def test_func(self):
        return get_object_or_404(Subscription, owner=self.request.user)
