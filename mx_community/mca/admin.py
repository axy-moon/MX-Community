from django.contrib import admin
from .models import *
from chat.models import *

# Register your models here.

admin.site.register(NewUser)
admin.site.register(Post)
admin.site.register(tokens)

admin.site.register(ChatMessage)

class ChatMessage(admin.TabularInline):
    model = ChatMessage

class ThreadAdmin(admin.ModelAdmin):
    inlines = [ChatMessage]
    class Meta:
        model = Thread

admin.site.register(Thread,ThreadAdmin)