# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Image,Location,Category


# Create your tests here.
class ImageTestCases(TestCase):
    """
    This is the class we will use to test the images
    """
    
    def setUp(self):
        """
        This will create a new image before each test case
        """
        funny = Category(name = "funny")
        funny.save()
        africa = Location(name = "Africa")
        africa.save()
        self.new_image = Image(name = "image",description = "h",location = africa,category = funny)
    
    def tearDown(self):
        """
        This will clear the db after each test
        """
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

    def test_instance(self):
        """
        This will test whether the new image created is an instance of the Image class
        """
        self.assertTrue(isinstance(self.new_image, Image))

    def test_init(self):
        """
        This will test whether the new image is instantiated correctly
        """
        self.assertTrue(self.new_image.name == "image")


