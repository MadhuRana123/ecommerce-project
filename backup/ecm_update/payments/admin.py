from django.contrib import admin
from .models import * 
    
@admin.register(Products)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','stripe_product_id']

@admin.register(Price)
class PriceModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'stripe_price_id','price']
