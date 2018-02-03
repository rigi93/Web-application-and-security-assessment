from __future__ import unicode_literals

from django.db import models

from datetime import datetime

# Creating models here.
# model is created. These are the fields stored in the form of a table in the database
class uploadimg(models.Model):
	# description is the caption provided by the user. The default value is blank and takes max of 30 characters
	description = models.CharField(max_length = 30, default = "")
# The image Url is stored pointing towards the folder pics where actual images are stored
	usr_image = models.ImageField(upload_to = 'pics')
# Date field is not supposed to be entered by user hence kept blank.
	usr_date = models.DateTimeField(default = datetime.now, blank = True)





