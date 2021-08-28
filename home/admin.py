from django.contrib import admin
from home.models import Apointment, Contact, High_admission, Pri_admission, Re_admission

# Register your models here.
admin.site.register(Contact)
admin.site.register(Apointment)
admin.site.register(High_admission)
admin.site.register(Pri_admission)
admin.site.register(Re_admission)