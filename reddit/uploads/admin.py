from django.contrib import admin

# Register your models here.
from uploads.models import Posts
from users.models import User

admin.site.register(User)
admin.site.register(Posts)
