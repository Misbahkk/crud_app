from django.contrib import admin
from .models import Member
# Register your models here.


class Memberadmin(admin.ModelAdmin):
    list_display = 'firstname', 'lastname', 'department', 'email'


admin.site.register(Member,Memberadmin)