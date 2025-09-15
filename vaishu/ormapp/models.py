from django.db import models
from django.contrib import admin
class Car(models.Model):
    car_no=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=15)
    model=models.CharField()
    email=models.EmailField()
    produce_date=models.IntegerField()
class CarAdmin(admin.ModelAdmin):
    list_display=["car_no","name","model","email","produce_date"]


























