from __future__ import unicode_literals
from django.db import models
import datetime

TYPE_CHOICES = (
        ('Bar Graph', 'Bar Graph'),
        ('Line Graph', 'Line Graph'),
        ('Pie Graph','Pie Graph'),
    )
class User(models.Model):
    	name=models.CharField(max_length=30)
    	type_Of_Graph=models.CharField(max_length=10,choices=TYPE_CHOICES,default=1)
        x_Attribute=models.CharField(max_length=10)
        y_Attribute=models.CharField(max_length=10)
        #Upload_CSV_File=models.FileField(upload_to='/files/')

    	class Admin:
    				pass

    	def __str__(self):
    		return '%s %s' % (self.name)
