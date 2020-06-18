from django.contrib import admin
from . models import Rooms, Service

class RoomsAdmin(admin.ModelAdmin):
    list_display = ('name','check_in_date','check_out_date','number_of_guests','room_number','all_services','price','active','created_date','update_date',)
admin.site.register(Rooms, RoomsAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display=('name','active','created_date','update_date',)
admin.site.register(Service,ServiceAdmin)
