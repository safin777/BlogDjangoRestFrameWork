from django.contrib import admin
from .models import Post


# Register your models here.

admin.site.register(Post)  # This is the only line of code we need to register 
                           #our model with the admin site
