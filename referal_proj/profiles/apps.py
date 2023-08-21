from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    name = "profiles"
    default_app_config = "profiles.apps.ProfilesConfig"

    def ready(self):
        import profiles.signals
