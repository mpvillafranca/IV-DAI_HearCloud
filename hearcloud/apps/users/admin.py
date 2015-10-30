from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdmin(UserAdmin):
	fieldsets = (
		('Users',{'fields' : ('username', 'password')}),
		('Personal Info',{'fields' : ('first_name',
										'last_name',
										'email',
										'avatar')}),
		('Permissions',{'fields' : ('is_active',
									'is_staff',
									'is_superuser',
									'groups',
									'user_permissions')}),
	)
# Register your models here.
admin.site.register(User,UserAdmin)
