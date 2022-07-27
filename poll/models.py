from django.db import models

# Create your models here.

QuantChoices = [(1,1),(2,2),(3,3)]

class Fruit(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    taste = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True, choices=QuantChoices)

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

class Publication(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=100, null=True, blank=True)
    publication = models.ManyToManyField(Publication)

    