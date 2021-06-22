from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    label = 'users'
    verbose_name = 'Users'

    def ready(self):
        import users.signals