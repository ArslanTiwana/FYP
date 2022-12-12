from operator import truediv
from django.db import models
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File


class Person(models.Model):
    First_Name=models.CharField(max_length=20,null=True)
    Last_Name=models.CharField(max_length=20,null=True)

    CNIC=models.CharField(max_length=15,null=True)
    Phone_Number=models.BigIntegerField(null=True)
    class Meta:
        abstract=True

class Car(models.Model):
    Car_Plate_number=models.CharField(max_length=7,primary_key=True)
    Name=models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.Car_Plate_number

class Card(models.Model):
    Card_id=models.AutoField(primary_key=True)
    Car_Plate_number=models.ForeignKey(Car, null=True,on_delete=models.SET_NULL)
    Barcode_id=models.IntegerField(unique=True)
    barcode=models.ImageField(upload_to='static/barcodeimages/',blank=True)
    type=models.CharField(max_length=20,default="resident")
    def __int__(self):
        return self.Card_id
    def save(self,*args,**kwargs):
        Ean=barcode.get_barcode_class('ean13')
        ean=Ean(str(self.Barcode_id),writer=ImageWriter())
        Buffer=BytesIO()
        ean.write(Buffer)
        self.barcode.save(str(self.Barcode_id)+'.png',File(Buffer),save=False)
        return super().save(*args,**kwargs)


class Driver(Person):
    Card_id=models.ForeignKey(Card,blank=True,null=True,on_delete=models.SET_NULL)
    Car_Plate_number=models.ForeignKey(Car, null=True,on_delete=models.SET_NULL)
    House_no=models.CharField(max_length=200,blank=True,null=True)
    Street=models.CharField(max_length=200,blank=True,null=True)
    Sector=models.CharField(max_length=200,blank=True,null=True)
    Sector=models.CharField(max_length=200,blank=True,null=True)
    type=models.CharField(max_length=20,default="resident")

    class Meta:

        abstract=True
class Residents(Driver):
    Resident_id=models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.First_Name
    
class Guests(Driver):
    Guest_id=models.AutoField(primary_key=True)
    isentered=models.BooleanField(default=False)
    Phone_Number=None
    def __str__(self):
        return self.First_Name
class Admin(Person):
    Admin_id=models.IntegerField()

class temproryresidentdata(models.Model):
    R_id=models.AutoField(primary_key=True)
    First_Name=models.CharField(max_length=20,null=True)
    Last_Name=models.CharField(max_length=20,null=True)
    CNIC=models.CharField(max_length=15,null=True)
    Phone_Number=models.BigIntegerField(null=True)
    Car_Name=models.CharField(max_length=30,null=True)
    Car_Plate_number=models.CharField(max_length=7,unique=True)
    House_no=models.CharField(max_length=200,blank=True,null=True)
    Street=models.CharField(max_length=200,blank=True,null=True)
    Sector=models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.First_Name
    
class history(models.Model):
    Guest_id=models.BigIntegerField()
    Entry_time=models.DateTimeField(blank=True,null=True,default=None)
    Exit_time=models.DateTimeField(blank=True,null=True,default=None)
    def __int__(self):
        return self.Guest_id

    
# Create your models here.
