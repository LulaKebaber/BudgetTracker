from django.contrib import admin
from .models import Person, Expense, Settlement

admin.site.register(Person)
admin.site.register(Expense)
admin.site.register(Settlement)