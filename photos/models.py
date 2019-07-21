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

    def save_image(self):
        """
        This is the function that we will use to save the instance of this class
        """
        self.save()

    def delete_image(self):
        """
        This is the function that we will use to delete the instance of this class
        """
        Image.objects.get(id = self.id).delete()

    def update_image(self,val):
        """
        This is the method to update the instance
        """
        Image.objects.filter(id = self.id).update(name = val)
    
     @classmethod
    def get_image_by_id(cls,image_id):
        """
        This is the method to get a specific image
        """
        return cls.objects.get(id = image_id)

    @classmethod
    def get_all_images(cls):
        all_images = Image.objects.all()
        return all_images

     @classmethod
    def search_image(cls,search_category):
        images_category = Image.objects.filter(category__photo_category__icontains=search_category)
        return images_category


    


