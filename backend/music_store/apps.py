from django.apps import AppConfig


class MusicStoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'music_store'
    verbose_name: str = 'Music Store'