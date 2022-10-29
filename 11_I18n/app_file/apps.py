from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppFileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_file'
    verbose_name = _('Файл')
    verbose_name_plural = _('Файлы')