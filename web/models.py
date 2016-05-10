from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.timezone import now

# Create your models here.

class Page(models.Model):
	name = models.CharField(max_length=200)
	active = models.BooleanField(default=True)
	menu = models.BooleanField(default=True)
	creation_date = models.DateTimeField(default=now())
	modified_date = models.DateTimeField()
	order = models.IntegerField(default=0)
	text = RichTextField()
	def __unicode__(self):
		return self.name
