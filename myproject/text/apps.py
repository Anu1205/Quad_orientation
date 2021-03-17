from django.apps import AppConfig
class textConfig(AppConfig):
    name = 'text'
    def contentextraction(self,content):
        name=content.lower()
        return {"con":name}