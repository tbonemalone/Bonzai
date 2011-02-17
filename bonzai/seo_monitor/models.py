from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
# work on models with ryan today. Need to get them set up correctly

# rename this model django has a different site model that they give you.
class Site(models.Model): 
	"""model for a site"""
	user = models.ForeignKey(User)
	tld = models.URLField()
	xml_sitemap_loc = models.URLField() #change name to xml_sitemap_uri
	
	def __unicode__(self):
		"""docstring for __unicode__"""
		return self.tld

class Page(models.Model):
	"""Model for a page"""
	url = models.URLField()
	keyword = models.CharField(max_length=100) #change to manyToMany relationship use through relationship
	title_tag = models.CharField(max_length=100)
	h1_tag = models.CharField(max_length=50)
	last_date_audited = models.DateTimeField()
	site = models.ForeignKey(Site)
	
	def __unicode__(self):
		"""docstring for __unicode__"""
		return self.url
# create new keyword model use many to many relationship for pages