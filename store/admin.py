from django.contrib import admin
from .models import Category, Customer, Product, Order


admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
