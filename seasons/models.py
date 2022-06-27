from django.db import models


# Create your models here.

class Season(models.Model):
    
    class Meta:

        verbose_name = "Season"
        verbose_name_plural = "Seasons"

    title = models.CharField(max_length=255, blank=True, null=True, unique=True)

    number = models.PositiveSmallIntegerField(unique=True)
    # latin numeral
    numeral = models.CharField(max_length=5, unique=True)

    description = models.TextField()



    def __str__(self):
        return f"Season #{self.number}"


class Nft(models.Model):

    pass