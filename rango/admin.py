from django.contrib import admin
from rango.models import Category, Page


class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('name',)}
	
admin.site.register(Category,CategoryAdmin)

# Register your models here.
class PageAdmin(admin.ModelAdmin):
	list_display=('title','category','url')#调换顺序
	###未完

admin.site.register(Page,PageAdmin)	