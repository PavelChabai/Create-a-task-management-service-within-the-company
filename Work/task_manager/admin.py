from django.contrib import admin
from .models import User,Customer,Employee,Task


admin.site.register(Customer)
admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Task)
