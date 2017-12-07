from django.contrib import admin

# Register your models here.
from CollabCheckout.models import RoomSlot

class RoomSlotAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User input', {'fields': ['checkout_email', 'reserved']}),
        ("Slot information (don't change)", {'fields': ['date', 'day_type','period', 'start_time', 'end_time','room'], 'classes':['collapse']}),
    ]
    list_filter = ['date', 'room', 'period', 'reserved']
    search_fields = ['date', 'checkout_email', 'reserved']

admin.site.register(RoomSlot, RoomSlotAdmin)