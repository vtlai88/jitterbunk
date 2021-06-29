from django.contrib import admin
from .models import User, Bunk

# Register your models here.
# making the app modifiable by the admin

admin.site.register(User)
admin.site.register(Bunk)