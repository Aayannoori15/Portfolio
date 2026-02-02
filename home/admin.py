from django.contrib import admin

# Register your models here.
from home.models import *

admin.site.register(experience)
admin.site.register(education)
admin.site.register(project)
admin.site.register(achievements)
admin.site.register(certifications)