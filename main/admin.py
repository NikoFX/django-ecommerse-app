from django.contrib import admin
from .models import Calls

# Register your models here.
@admin.register(Calls)
class CallsAdmin(admin.ModelAdmin):

    list_display = ('name', 'phone', 'message', 'created_date', 'status')

    fields = ('name', 'phone', 'message', 'created_date', 'status')
    readonly_fields = ('name', 'phone', 'message', 'created_date')


    class Meta:
        model = Calls
