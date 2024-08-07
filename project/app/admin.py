from django.contrib import admin
from .models import CustomUser,Marks
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Marks)