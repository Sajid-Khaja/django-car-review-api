from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator,MaxLengthValidator

def alphanumeric(value):
    if not str(value).isalnum():
        raise ValidationError("Value must be alphanumeric")
    return value


class Showroom(models.Model):
    name=models.CharField(max_length=30)
    location=models.CharField(max_length=50)
    website=models.URLField(max_length=100)
    def __str__(self):
        return f"{self.name},{self.location}" 

class Car(models.Model):
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=30)
    active=models.BooleanField(default=False)
    price=models.DecimalField(max_digits=9,decimal_places=2,blank=True,null=True)
    chassisnumber=models.CharField(max_length=100,blank=True,null=True,validators=[alphanumeric])
    showroom_visit = models.ForeignKey(Showroom, on_delete=models.CASCADE, related_name='cars', null=True)


    # realted names are used in nested seriializers     

    def __str__(self):
        return f"id is : {self.id}, {self.name}, chassisnumber : {self.chassisnumber}"
    

class Review(models.Model):
    rating=models.IntegerField(validators=[MaxLengthValidator,MinLengthValidator])
    comments=models.CharField(max_length=200,null=True)
    car=models.ForeignKey(Car , on_delete=models.CASCADE, related_name='REV',null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f" the rating of {self.car.name} is {self.rating}, {self.comments}"


