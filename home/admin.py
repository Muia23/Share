from django.contrib import admin
from .models import location,category,Post

class PostAdmin(admin.ModelAdmin):
    filter_horizontal =('location', 'category',)
# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(location)
admin.site.register(category)



