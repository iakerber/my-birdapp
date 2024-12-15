from django.contrib import admin
from .models import Waterbird, Raptor, Songbird

# Register your models here.
admin.site.register(Waterbird)
admin.site.register(Raptor)
admin.site.register(Songbird)