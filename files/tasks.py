from .models import Bumps
from bumpahead_server.celery import app
from django.conf import settings
from oct2py import Oct2Py
# from oct2py import Oct2Py
@app.task
def analyser(filename):
	oct = Oct2Py()
	oct.addpath(settings.MEDIA_ROOT)
	ans = oct.appcode3(filename)
	for value in ans:
		latt = float(value[0])
		longt = float(value[1])
		for_saving = Bumps(longitude=longt, lattitude=latt)
		for_saving.save()
	

# with open(settings.MEDIA_ROOT+"/"+filename,"r") as readings:
		# for line in readings:
		# 	fields = line.split(':')
		# 	temp = fields[8]
		# 	temp = temp[0:8]
		# 	acc = float(temp)
		# 	if acc > 15 or acc < 5:
		# 		# print fields[4:6]
		# 		# print("\n")
		# 		longt = float(fields[4])
		# 		latt = float(fields[5])
		# 		for_saving = Bumps(longitude=longt, lattitude=latt)
		# 		for_saving.save()