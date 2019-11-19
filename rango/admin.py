from django.contrib import admin
from rango.models import Category, Page

admin.site.register(Category)



# Register your models here.
class PageAdmin(admin.ModelAdmin):
	list_display=('title','category','url')
	###未完

admin.site.register(Page,PageAdmin)	