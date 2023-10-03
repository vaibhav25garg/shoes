from django.contrib import admin
from .models import Product,Customer

# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','selling_price','discription','product_image1',]

@admin.register(Customer)
class CustmerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','zipcode','state'] 