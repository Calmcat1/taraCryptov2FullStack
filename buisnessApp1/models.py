from django.db import models

# Create your models here.

#TODO: when i reach home to try and get the postgres server to work so i can have my site up{done}

# this is the Table storing the headline content
class blogHeadlineTable(models.Model):
    blogTitle = models.CharField(max_length=255, default='null')
    blogSummary = models.CharField(max_length=255, default='null')
    blogAuthor = models.CharField(max_length=255, default='null')
    blogContent = models.CharField(max_length=2500, default='null')
    blogContent1 = models.CharField(max_length=2500, default='null')
    blogImageLinks = models.CharField(max_length=255, default='null')
    


class productsTable(models.Model):
    productName = models.CharField(max_length=255)
    productDesc = models.CharField(max_length=255)
    productPrice = models.IntegerField(default=0)
    productImageLinks = models.CharField(max_length=255, default='null')

