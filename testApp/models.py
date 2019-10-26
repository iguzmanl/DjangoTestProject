from django.db import models

# Create your models here.

class Visitor(models.Model):
	visit_date = models.DateField()
	visit_time = models.TimeField()
