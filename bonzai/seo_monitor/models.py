from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Site(models.Model):
	"""modelf for a site"""
	tld = models.URLField()
	xml_sitemap_loc = models.URLField()

class Page(models.Model):
	"""Model for a page"""
	url = models.URLField()
	keyword = models.CharField()
	title_tag = models.CharField()
	h1_tag = models.CharField()
	last_date_audited = models.DateTimeField()
	site = models.ForeignKey(Site)
	