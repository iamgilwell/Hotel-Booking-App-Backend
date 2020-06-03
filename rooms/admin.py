from django.contrib import admin
from . models import Rooms

class RoomsAdmin(admin.ModelAdmin):
    list_display = ('name','check_in_date','check_out_date','number_of_guests','room_number','active','created_date','update_date',)
admin.site.register(Rooms, RoomsAdmin)
