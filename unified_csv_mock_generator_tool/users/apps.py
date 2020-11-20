from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "unified_csv_mock_generator_tool.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import unified_csv_mock_generator_tool.users.signals  # noqa F401
        except ImportError:
            pass
