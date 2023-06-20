from django.contrib import admin

# Register your models here.
from .models import AboutUs
from .models import Home
from .models import Carusel
admin.site.register(Home)
admin.site.register(AboutUs)
admin.site.register(Carusel)

