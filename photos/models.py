# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Location(models.Model):
    """
    This is the class where we will create locations
    """
    name = models.CharField(max_length = 30)

    def save_location(self):
        """
        This is the function that we will use to save the instance of this class
        """
        self.save()

    def delete(self):
        """
        This is the method to delete the instance
        """
        self.delete()

    def update(self,field,val):
        """
        This is the method to update the instance
        """
        Location.objects.get(id = self.id).update(field = val)

    def __str__(self):
        return self.photo_location

class Category(models.Model):
    """
    This is the class where we will create categories
    """
    name = models.CharField(max_length = 30)
    def save_category(self):
        """
        This is the function that we will use to save the instance of this class
        """
        self.save()

    def delete(self):
        """
        This is the method to delete the instance
        """
        Category.objects.get(id = self.id).delete()

    def update(self,field,val):
        """
        This is the method to update the instance
        """
        Category.objects.get(id = self.id).update(field = val)

    def __str__(self):
        return self.name
class Image(models.Model):
    """
    This is the class we will use to create images
    """
    image_url = models.ImageField(upload_to = "images/")
    name = models.CharField(max_length = 30)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)


