from django.contrib import admin
from .models import Package, Venue, Events, User, Extra
# Register your models here.

admin.site.register(Package)
admin.site.register(Venue)
admin.site.register(Events)
admin.site.register(User)
admin.site.register(Extra)
