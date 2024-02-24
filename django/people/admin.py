# imports Django
from django.contrib import admin

# imports, this app
from .models import User


admin.site.register(User)