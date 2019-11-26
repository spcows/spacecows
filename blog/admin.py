from django.contrib import admin
from .models import Post, Category, Comment

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
