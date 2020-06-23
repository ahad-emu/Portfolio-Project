from django.contrib import admin
from .models import PythonBlog, DjangoBlog
# Register your models here.

admin.site.register(PythonBlog)
admin.site.register(DjangoBlog)
