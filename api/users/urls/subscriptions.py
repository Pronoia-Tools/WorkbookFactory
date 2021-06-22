from django.urls import path
from users import views

urlpatterns = [
    # Users paths

    # The profile edit view
    path('payment/',
         views.SubscriptionPayment.as_view(), name="subscription_payment"),

    # get the stripe config
    path('config/', views.stripe_config),

    # create the checkout session
    path('create-checkout-session/', views.create_checkout_session),

    # add subscription
    path('add-subscription/', views.update_subscription),

    # The profile edit view
    path('success/', views.SubscriptionSuccess.as_view()),

    # The profile edit view
    path('cancelled/', views.SubscriptionCancelled.as_view()),

     # The profile edit view
    path('webhook/', views.stripe_webhook),
]
