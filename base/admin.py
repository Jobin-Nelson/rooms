from django.contrib import admin
from .models import Room, Topic, Message

# Register your models here.

custom_models = [
    Room,
    Topic,
    Message,
]

for model in custom_models:
    admin.site.register(model)
