from django.db import models

# Create your models here.

class Post (models.Model):
	title = models.CharField(max_length=200)
	image = models.FileField(upload_to="images/")
	description = models.TextField()
	pub_date = models.DateTimeField('date published')
        
        def __unicode__(self):
            return self.title

#class Tag(models.Model):
#	tag = models.CharField(max_length=200)
#
#
#class Comments(models.Model):
#	identity = models.CharField(max_length=64)
#	mail = models.CharField(max_length=64)
#	comment = models.CharField(max_length=200)
#	date = models.DateTimeField('date published')
