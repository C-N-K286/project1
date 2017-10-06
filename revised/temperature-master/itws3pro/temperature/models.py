# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Temperature(models.Model):
	tem_value = models.CharField(max_length=250)
	hum_value = models.CharField(max_length=250)
	soil_mois = models.CharField(max_length=250)
	wat_lvl = models.CharField(max_length=250)
	time = models.CharField(max_length=250)
	def __str__(self):
		return str(self.tem_value + "," + self.hum_value + "," + self.soil_mois+','+self.wat_lvl+','+self.time)
