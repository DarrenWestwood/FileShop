from django.contrib import admin
from .models import Order, Product, File

# Register your models here.

admin.site.register(Order)
admin.site.register(File)
admin.site.register(Product)
