from django.contrib import admin
from .models import (FAQ, Contact, New, Discount, Rent, Immovables, Doctor, RequestRent, RequestImm, Comment, Report,
                     Vacancion)

admin.site.register(FAQ)
admin.site.register(Contact)
admin.site.register(New)
admin.site.register(Discount)
admin.site.register(Doctor)
admin.site.register(Rent)
admin.site.register(Immovables)
admin.site.register(RequestRent)
admin.site.register(RequestImm)
admin.site.register(Comment)
admin.site.register(Report)
admin.site.register(Vacancion)
