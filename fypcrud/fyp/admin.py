from django.contrib import admin
from fyp.models import Person
from fyp.models import Car
from fyp.models import Card
from fyp.models import Driver
from fyp.models import Residents
from fyp.models import Guests
from fyp.models import Admin
from fyp.models import history
admin.site.register(Car)
admin.site.register(Card)
#admin.site.register(Driver)
admin.site.register(Residents)
admin.site.register(Guests)
admin.site.register(Admin)
admin.site.register(history)

# Register your models here.
