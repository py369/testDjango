
from django.contrib import admin
from .models import Post
from .models import Voetbalspelers

class VoetbalspelersAdmin(admin.ModelAdmin):
    exclude = ('title', 'text')

admin.site.register(Post)
admin.site.register(Voetbalspelers, VoetbalspelersAdmin)

