from django.contrib import admin
from .models import Location,Post,tags

class PostAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)
# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Location)
admin.site.register(tags)




