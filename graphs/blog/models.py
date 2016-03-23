from __future__ import unicode_literals

from django.db import models

import datetime

class User(models.Model):
    	name = models.CharField(max_length=30)
    	type_graph=models.CharField(max_length=10)
        x=models.CharField(max_length=10)
        y=models.CharField(max_length=10)

    	class Admin:
    				pass

    	def __str__(self):
    		return '%s %s' % (self.name)
