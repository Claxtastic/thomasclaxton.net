from django.contrib import admin
from apps.about.models import Resume

# Register your models here.

class ResumeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Resume, ResumeAdmin)
