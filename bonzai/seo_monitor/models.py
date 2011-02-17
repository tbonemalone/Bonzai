from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

# rename this model django has a different site model that they give you.
class Site(models.Model): 
	"""model for a site"""
	tld = models.URLField()
	xml_sitemap_loc = models.URLField() #change name to xml_sitemap_uri

class Page(models.Model):
	"""Model for a page"""
	url = models.URLField()
	keyword = models.CharField(max_length=100) #change to manyToMany relationship use through relationship
	title_tag = models.CharField(max_length=100)
	h1_tag = models.CharField(max_length=50)
	last_date_audited = models.DateTimeField()
	site = models.ForeignKey(Site)
	
# create new keyword model use many to many relationship for pages