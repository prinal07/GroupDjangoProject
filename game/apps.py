from django.apps import AppConfig


# class PlayerConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'game'

#     def ready(self):
#         pass

class GameConfig(AppConfig):
    name = 'game'

    def ready(self):
        import game.signals