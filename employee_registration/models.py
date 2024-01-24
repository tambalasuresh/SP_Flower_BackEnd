from django.db import models

class Position(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class EmpRegistration(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    number = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class EmpDetails(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    number = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    name=models.CharField(max_length=200)
    comment=models.TextField(null=True)

    def __str__(self):
        return self.name


class ShoopingCheckOut(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    number=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    pincode=models.CharField(max_length=100)
    door_number=models.CharField(max_length=100)
    area=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    conutry=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
