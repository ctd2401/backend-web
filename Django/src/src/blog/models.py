from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title       = models.CharField(max_length=120)# max_length=required
    author      = models.CharField(max_length=24)
    content     = models.TextField(blank=False,null=True)
    date        = models.DateTimeField()
    featured    = models.BooleanField(default=False)# null=True , default=True
    
    def get_absolute_url(self):
        return reverse("blog:article-detail",kwargs={"id": self.id})#f"/products/{self.id}"