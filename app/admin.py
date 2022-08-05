from django.contrib import admin
from .models import  (
    Customer,
    Product,
    Cart,
    OrderPlaced
)
# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register (Cart)
admin.site.register(OrderPlaced)


# @admin.register(Customer)
# class CustomerModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user','name','locality','city','pincode','state']

# @admin.register(Product)
# class ProductModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'sellingprice','discounted_price','description','brand',' category',' product_image']

# @admin.register(Cart)
# class CartModelAdmin(admin.ModelAdmin):
#     list_display = ['id','user','product','quantity']

# @admin.register(OrderPlaced)
# class OrderPlacedModelAdmin(admin.ModelAdmin):
#     list_display = ['id','user','customer','product','quantity','ordered_date','status']