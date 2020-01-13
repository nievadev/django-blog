from django.contrib import admin
from .models import Post

# Register Post table into the admin site (/admin)
admin.site.register(Post)
