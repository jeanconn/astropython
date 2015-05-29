from django.contrib import admin

from category.models import Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'subtitle', 'slug')
    list_filter = ('sites',)


admin.site.register(Category, CategoryAdmin)