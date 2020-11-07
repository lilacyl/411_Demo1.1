from django.contrib import admin

# Register your models here.
from .models import Test, StockInfo

admin.site.register(Test)
admin.site.register(StockInfo)