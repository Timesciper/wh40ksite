from django.apps import AppConfig

# app for managing missions (tables, terrain)


class MissionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'missions'
