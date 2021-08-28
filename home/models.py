from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=12, null=True)
    text_area=models.TextField(null=True)
    date=models.DateField()

    ############ for returning a table with name #############
    
    def __str__(self):
        return self.name

class Apointment(models.Model):
    a_name=models.CharField(max_length=50)
    a_email=models.CharField(max_length=100)
    a_phone_no=models.CharField(max_length=12, null=True)
    a_text_area=models.TextField(null=True)
    date=models.DateField()

    def __str__(self):
        return self.a_name

class High_admission(models.Model):
    student_name=models.CharField(max_length=50, null=True)
    student_email=models.CharField(max_length=100, null=True)
    student_phone_no=models.CharField(max_length=12, null=True)
    student_class=models.CharField(max_length=100, null=True)
    student_text_area=models.TextField(null=True)
    date=models.DateField()

    def __str__(self):
        return self.student_name

class Pri_admission(models.Model):
    student_name=models.CharField(max_length=50, null=True)
    student_email=models.CharField(max_length=100, null=True)
    student_phone_no=models.CharField(max_length=12, null=True)
    student_class=models.CharField(max_length=100, null=True)
    student_text_area=models.TextField(null=True)
    date=models.DateField()

    def __str__(self):
        return self.student_name

class Re_admission(models.Model):
    student_name=models.CharField(max_length=50, null=True)
    student_email=models.CharField(max_length=100, null=True)
    student_phone_no=models.CharField(max_length=12, null=True)
    student_class=models.CharField(max_length=100, null=True)
    student_text_area=models.TextField(null=True)
    date=models.DateField()

    def __str__(self):
        return self.student_name