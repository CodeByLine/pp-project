from django.db import models
from datetime import datetime


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    blog_text = models.TextField(max_length=500)
    image = models.ImageField(upload_to='portfolio/images', blank=True)
    url = models.URLField(blank=True)
    pub_date = models.DateTimeField(default=datetime.now)
