from django.contrib import admin
from .models import Employee,Product,Book,Movie,Student

# Register your models here.
admin.site.register(Employee)
admin.site.register(Product)
admin.site.register(Book)
admin.site.register(Movie)
admin.site.register(Student)

