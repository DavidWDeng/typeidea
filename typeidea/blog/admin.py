from django.contrib import admin

# Register your models here.
from .models import Post,Tag,Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','status','is_nav','created_time')
    fields=('name','status','is_nav')

    def save_model(self, request, obj, form, change):
        obj.owner=request.user
        return super().save_model(request, obj, form, change)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=('name','status','created_time')
    fields=('name','status')

    def save_model(self, request, obj, form, change):
        obj.owner=request.user
        return super().save_model(request, obj, form, change)