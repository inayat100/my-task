from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.create_invoice,name="create_invoice"),
    path('api/',views.create_invoice_api,name="create_invoice_api"),
    path('item-api/',views.add_item_api,name="add_item_api"),
    path('add-item/',views.add_item,name="add_item"),
 
]