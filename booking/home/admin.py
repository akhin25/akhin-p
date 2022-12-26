from django.contrib import admin
#from django.contrib import ModelAdmin
from.models import Contact

from.models import Departments,Doctors,Booking

# Register your models here.
admin.site.register(Departments)
admin.site.register(Doctors)
admin.site.register(Contact)

class BookingAdmin(admin.ModelAdmin):
    list_display=('id','p_name','p_phone','p_email','doc_name','booking_date','booked_on')

admin.site.register(Booking,BookingAdmin)

