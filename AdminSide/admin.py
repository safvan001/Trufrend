from django.contrib import admin
from AdminSide.models import Stories,DoctorData,Quotes,Languages
from django.contrib.auth.admin import UserAdmin
# from .models import DoctorData,Stories

# admin.site.register(DoctorData)
# admin.site.register(Languages)
# admin.site.register(Specality)
# Register your models here.
# class DoctorDataAdmin(UserAdmin):
#     list_display = ('id', 'username', 'Dp', 'is_staff', 'is_superuser')  # Customize as needed
#     fieldsets = UserAdmin.fieldsets + (
#         ('Custom Fields', {'fields': ('Dp',)}),  # Add other custom fields here
#     )
admin.site.register(Stories)
admin.site.register(Languages)
admin.site.register(DoctorData)
admin.site.register(Quotes)

