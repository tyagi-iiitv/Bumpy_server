from django.forms import widgets
from rest_framework import serializers
# from .models import Files, Bumps
from .models import Bumps

# class FileSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Files
# 		fields = ['files']

class BumpSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bumps
		fields = ['id','longitude','lattitude']