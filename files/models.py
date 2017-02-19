from django.db import models

# Create your models here.
class Files(models.Model):
	created = models.DateTimeField(auto_now_add=True, primary_key=True)
	docfile = models.FileField()


class Bumps(models.Model):
	longitude = models.FloatField()
	lattitude = models.FloatField()