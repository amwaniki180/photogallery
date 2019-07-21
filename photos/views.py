# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Image, Location, Category

# Create your views here.
def index(request):
    title = 'Home'
    images = Image.get_all_images()
    locations = Location.objects.all()
    return render(request, 'index.html', {'title':title, 'images':images, 'locations':locations})
    
def single_image(request, category_name, image_id):
    # print(image_category)
    locations = Location.objects.all()


