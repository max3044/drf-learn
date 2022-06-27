from django.db import models

# Create your models here.
class User(models.Model):
    
    name = models.CharField(max_length=155, blank=True, null=True)
    address = models.CharField(50, unique=True)

    # minted_nfts = models.ManyToManyField(to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
