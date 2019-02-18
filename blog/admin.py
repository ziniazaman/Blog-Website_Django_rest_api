from django.contrib import admin
from .models import Category, Article, Tag


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', )
    list_filter = ('name', )
    search_fields = ('name', )

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'get_tags', 'body',  )
    list_filter = ('title', 'body', )
    search_fields = ('title', 'body', )


admin.site.register(Category, CategoryAdmin)


admin.site.register(Article, ArticleAdmin)

admin.site.register(Tag)