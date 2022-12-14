import random
import os
from django.db import models

def get_filename_ext(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(filename)
    return name, ext
    
def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1,4000000000)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)
    
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=19, default=50.00)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    
    def __str__(self):
        return self.title