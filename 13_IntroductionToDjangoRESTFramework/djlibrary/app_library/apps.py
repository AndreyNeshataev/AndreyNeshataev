from django.apps import AppConfig


class AppLibraryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_library'
    verbose_name = 'Библиотека'
    verbose_name_plural = 'Библиотеки'
