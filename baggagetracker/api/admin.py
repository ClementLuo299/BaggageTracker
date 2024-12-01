from django.contrib import admin
from .models import Employee, Usr, Airline, Airplane, Airport

# Register your models here.
admin.site.register(Usr)
admin.site.register(Employee)
admin.site.register(Airline)
admin.site.register(Airplane)
admin.site.register(Airport)
