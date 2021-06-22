from flies.models import StarterFly
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from allauth.account.signals import email_confirmed
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse

import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

from .models import Account, Subscription

@receiver(post_save, sender=Account)
def create_related_subscription(sender, instance, created, *args, **kwargs):
    # Notice that we're checking for `created` here. We only want to do this
    # the first time the `User` instance is created. If the save that caused
    # this signal to be run was an update action, we know the user already
    # has a profile.
    if instance and created:
        # this will make them an auto subscribed user. Turn off after Beta

        Subscription.objects.create(owner=instance, subscribed=True, subscription_confirmed=True)

        # add them to the email list
        if instance.opt_in:

            mailchimp = MailchimpMarketing.Client()
            mailchimp.set_config({
                "api_key": settings.MAILCHIMP_KEY,
                "server": settings.MAILCHIMP_PREFIX
            })

            list_id = settings.MAILCHIMP_LIST

            email = instance.email

            member_info = {
                "email_address": instance.email,
                "status": "subscribed"
            }

            try:
                response = mailchimp.lists.add_list_member(list_id, member_info)
                print("response: {}".format(response))
            except ApiClientError as error:
                print("An exception occurred: {}".format(error.text))
