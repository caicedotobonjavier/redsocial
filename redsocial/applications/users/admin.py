from django.contrib import admin
#
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'email',
        'full_name',
        'phone',
        'address',
        'avatar',
        'date_birth',
        'cod_active',
        'otp_base32',
        'login_otp',
        'user_login_otp',
        'is_staff',
        'is_active', 
    )


admin.site.register(User, UserAdmin)