from django.contrib import admin
from .models import Sensor, Measurement


# Register your models here.

class MeasurementInline(admin.TabularInline):
    model = Measurement
    list_display = ['temperature', 'created_at']
    extra = 0

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    inlines = [MeasurementInline, ]
