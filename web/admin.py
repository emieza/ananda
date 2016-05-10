from django.contrib import admin
from datetime import datetime
from models import *

# Register your models here.

class PageAdmin(admin.ModelAdmin):
	readonly_fields = ('creation_date','modified_date',)
	list_display = ('name','active','order','modified_date')
	list_editable = ('order','active')
	ordering = ('order',)

	def save_model(self,request,page,form,change):
		page.modified_date = datetime.now()
		page.save()

admin.site.register( Page, PageAdmin )
