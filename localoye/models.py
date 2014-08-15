from django.db import models

class Venue(models.Model):
    name = models.CharField(max_length=128, unique=True)
    location = models.CharField(max_length=128)
    timestamp = models.DateTimeField()

    def __unicode__(self):
        return "%s - %s" % (self.name,self.location)

class Hall(models.Model):
	name = models.CharField(max_length=128,unique=True)
	venue = models.ForeignKey(Venue)
	capacity = models.IntegerField(default=0)
	price = models.IntegerField(default=0)

	def __unicode__(self):
		return "%s" % (self.name)