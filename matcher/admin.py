from django.contrib import admin

from models import (School, SchoolContact, SchoolSurvey, Policies, Expense,
                    Raiser, RaiserSurvey)

# Register your models here.
admin.site.register(School)
admin.site.register(SchoolContact)
admin.site.register(SchoolSurvey)
admin.site.register(Policies)
admin.site.register(Expense)
admin.site.register(Raiser)
admin.site.register(RaiserSurvey)

