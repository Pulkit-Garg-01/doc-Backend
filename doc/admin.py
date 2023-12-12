from django.contrib import admin
from .models import *
from rest_framework.authtoken.models import Token
# Register your models here.

admin.site.register(User)
admin.site.register(Document)
admin.site.register(Permission)
admin.site.register(Group)

