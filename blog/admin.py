from django.contrib import admin
from blog.models import SightseeingPlaces,Category

@admin.register(SightseeingPlaces)
class SightseeingPlacesAdmin(admin.ModelAdmin):
    fields=['name','slug','category','author','country','city','description']
    prepopulated_fields = {'slug':('name',)}
    search_fields = ['name','city','country']
    list_display = ['name','country','city','author']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['categoryName']

