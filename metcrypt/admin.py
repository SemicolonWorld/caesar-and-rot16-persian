from django.contrib import admin
from .models import EncryptAndDecryptModel

# Register your models here.

class EncryptAdmin(admin.ModelAdmin):
	list_display = (
		'text',
		'result',
		'encordec',
		'what_type',
	)

	list_filter =(
		'encordec',
		'what_type',
	)
	search_fields = (
		'text',
		'result',
	)

admin.site.register(EncryptAndDecryptModel, EncryptAdmin)