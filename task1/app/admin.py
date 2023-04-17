from django.contrib import admin
from .models import Buyer,Seller,Items,Invoice
# Register your models here.


admin.site.register(Seller)
admin.site.register(Buyer)
admin.site.register(Items)
admin.site.register(Invoice)
