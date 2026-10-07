from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=50)
    age=models.PositiveIntegerField()   
    email=models.EmailField(unique=True)
    doj=models.DateField(auto_now_add=True)
    address=models.CharField(blank=True,null=True)

    def __str__(self):
        return f"{self.name} {self.age} {self.address}"

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    describtion = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quality = models.IntegerField()
    category = models.CharField(max_length=100, default="General")
    brand = models.CharField(max_length=100, default="Unknown")
    is_avalables = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    Update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
class Book(models.Model):
    Book_title=models.CharField(max_length=50)
    Author_name=models.CharField(max_length=80)
    genre=models.CharField(max_length=100,blank=True)
    published_year=models.IntegerField()
    def __str__(self):
        return self.Book_title

class Movie(models.Model):
    Movie_title=models.CharField(max_length=100)
    Directer_name=models.CharField(max_length=100)
    relesed_date=models.DateField()
    language=models.CharField(max_length=50,default="English")
    def __str__(self):
        return self.Movie_title

class Student(models.Model):
    student_name=models.CharField(max_length=100)
    age = models.IntegerField()
    email_address=models.EmailField(unique=True)
    date_of_birth=models.DateField()
    course=models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.student_name
class Emp(models.Model):
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    def __str__(self):
        return self.name

class Employeeprofile(models.Model):
    emp=models.OneToOneField(Emp,on_delete=models.CASCADE)
    Address=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)

    def __str__(self):
        return self.emp.name
class Department(models.Model):
    titel=models.CharField(max_length=30)
    branch=models.CharField(max_length=30)

class Staffs(models.Model):
    name=models.CharField(max_length=100)
    experience=models.PositiveIntegerField(default=0)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    address=models.CharField(max_length=30,blank=True,null=True)
    phone=models.CharField(max_length=30,blank=True,null=True)

class Images(models.Model):
    image=models.ImageField(upload_to='image/',blank=True,null=True)
    description=models.CharField(max_length=500,blank=True,null=True)