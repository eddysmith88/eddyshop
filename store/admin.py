from django.contrib import admin
from .models import Category, Customer, Product, Order, Profile
from django.contrib.auth.models import User


admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Profile)


# Mix user info and profile info
class ProfileInline(admin.StackedInline):
    model = Profile


# Extend user model
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username", "email", "first_name", "last_name"]
    inlines = [ProfileInline]


# Unregister old way
# admin.site.register(User)

# Re-register the new way
# admin.site.register(User, UserAdmin)
