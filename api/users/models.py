# -*- coding: utf-8 -*-
import uuid
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
from django.utils.functional import cached_property
from allauth.account.models import EmailAddress
from .managers import AccountManager

from utils.models import Core
from utils.validators import phone_validator


class Account(AbstractBaseUser, Core, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(
        null=True, blank=True, max_length=100, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    first_name = models.CharField(null=True, blank=True, max_length=50)
    last_name = models.CharField(null=True, blank=True, max_length=50)
    opt_in = models.BooleanField(default=False, verbose_name="Add me to the Workbook Factory email list", help_text="Don't worry, we won't spam you.")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = AccountManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name


    @cached_property
    def emails(self):
        try:
            return EmailAddress.objects.filter(user=self).exclude(primary=True)
        except:
            pass

    @cached_property
    def all_emails(self):
        try:
            return EmailAddress.objects.filter(user=self)
        except:
            pass

    @cached_property
    def primary_email(self):
        try:
            return EmailAddress.objects.get(user=self, primary=True, verified=True)
        except:
            pass

    @cached_property
    def subscription(self):
        try:
            return Subscription.objects.get(owner=self)
        except:
            pass

    @cached_property
    def subscribed(self):
        try:
            return Subscription.objects.get(owner=self, subscribed=True)
        except:
            pass



class Subscription(models.Model):
    owner = models.OneToOneField("Account", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    archived = models.BooleanField(default=False)
    modified = models.DateTimeField(auto_now=True)
    subscribed = models.BooleanField(default=False)
    subscription_confirmed = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Subscription"
        verbose_name_plural = "Subscritions"

    def __str__(self):
        return self.owner.email

